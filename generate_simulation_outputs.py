import os
import sys
import subprocess
import shutil
from pathlib import Path

SITECUSTOMIZE_CONTENT = """import sys
import os
from pathlib import Path

# Ensure Matplotlib uses the Agg backend for headless execution
os.environ['MPLBACKEND'] = 'Agg'

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    
    # Save the original show function
    original_show = plt.show
    
    def patched_show(*args, **kwargs):
        script_path = Path(sys.argv[0]).resolve()
        outputs_dir = script_path.parent / "outputs"
        outputs_dir.mkdir(exist_ok=True)
        
        fignums = plt.get_fignums()
        if fignums:
            if len(fignums) == 1:
                fig = plt.figure(fignums[0])
                fig_path = outputs_dir / f"{script_path.stem}.png"
                fig.savefig(fig_path, dpi=150, bbox_inches='tight')
                print(f"[RUNNER] Saved plot to {fig_path}", file=sys.stderr)
            else:
                for idx, fignum in enumerate(fignums):
                    fig = plt.figure(fignum)
                    fig_path = outputs_dir / f"{script_path.stem}_fig{idx+1}.png"
                    fig.savefig(fig_path, dpi=150, bbox_inches='tight')
                    print(f"[RUNNER] Saved plot {idx+1} to {fig_path}", file=sys.stderr)
        
        original_show(*args, **kwargs)
        
    plt.show = patched_show
except Exception as e:
    # Quietly fail if matplotlib is not available in the environment
    pass
"""

def main():
    root_dir = Path(__file__).resolve().parent
    temp_runner_dir = root_dir / ".temp_runner"
    
    # Create temp directory and sitecustomize dynamically
    temp_runner_dir.mkdir(exist_ok=True)
    sitecustomize_file = temp_runner_dir / "sitecustomize.py"
    with open(sitecustomize_file, "w", encoding="utf-8") as f:
        f.write(SITECUSTOMIZE_CONTENT)
        
    try:
        # Get list of directories 01_ to 22_
        sim_dirs = []
        for p in root_dir.iterdir():
            if p.is_dir() and p.name[:2].isdigit() and 1 <= int(p.name[:2]) <= 22:
                sim_dirs.append(p)
                
        sim_dirs.sort(key=lambda p: int(p.name[:2]))
        
        # Set up environment with sitecustomize in PYTHONPATH
        env = os.environ.copy()
        env["PYTHONPATH"] = str(temp_runner_dir) + os.pathsep + env.get("PYTHONPATH", "")
        env["PYTHONIOENCODING"] = "utf-8"
        
        total_scripts = 0
        successful_runs = 0
        failed_runs = 0
        timeout_runs = 0
        
        print("=" * 60)
        print("Starting ECE Simulation Outputs Generator")
        print("=" * 60)
        
        for sim_dir in sim_dirs:
            print(f"\nProcessing directory: {sim_dir.name}")
            outputs_dir = sim_dir / "outputs"
            outputs_dir.mkdir(exist_ok=True)
            
            # Keep .gitkeep if it exists, or create one if outputs is empty
            gitkeep_file = outputs_dir / ".gitkeep"
            if not gitkeep_file.exists():
                with open(gitkeep_file, "w") as f:
                    f.write("")
            
            # Find all python scripts in this directory
            py_files = sorted([f for f in sim_dir.glob("*.py")])
            
            for py_file in py_files:
                if py_file.name == "generate_simulation_outputs.py":
                    continue
                    
                total_scripts += 1
                print(f"  Running {py_file.name}...", end="", flush=True)
                
                # Use shorter timeout for interactive files like chat_application_socket
                is_interactive = "chat_application_socket" in py_file.name
                timeout_sec = 2.0 if is_interactive else 25.0
                
                try:
                    # Run the simulation script
                    res = subprocess.run(
                        [sys.executable, str(py_file)],
                        capture_output=True,
                        text=True,
                        env=env,
                        cwd=str(sim_dir),
                        timeout=timeout_sec
                    )
                    
                    status = "SUCCESS" if res.returncode == 0 else "FAILED"
                    stdout = res.stdout
                    stderr = res.stderr
                    
                    if res.returncode == 0:
                        successful_runs += 1
                    else:
                        failed_runs += 1
                        
                except subprocess.TimeoutExpired as e:
                    status = "TIMEOUT"
                    stdout = e.stdout or ""
                    stderr = e.stderr or ""
                    if hasattr(e, 'output') and e.output:
                        stdout = e.output
                    stderr += f"\n[RUNNER] Process timed out after {timeout_sec} seconds."
                    timeout_runs += 1
                    
                # Post-process outputs
                log_path = outputs_dir / f"{py_file.stem}.txt"
                
                # Format the console log output file
                log_lines = []
                log_lines.append("=" * 80)
                log_lines.append(f"Simulation Output Log")
                log_lines.append(f"Script: {sim_dir.name}/{py_file.name}")
                log_lines.append(f"Status: {status}")
                log_lines.append("=" * 80)
                log_lines.append("")
                
                if stdout.strip():
                    log_lines.append("--- Standard Output ---")
                    log_lines.append(stdout.strip())
                    log_lines.append("")
                    
                if stderr.strip():
                    log_lines.append("--- Standard Error / Warnings ---")
                    log_lines.append(stderr.strip())
                    log_lines.append("")
                    
                if not stdout.strip() and not stderr.strip():
                    log_lines.append("No console output was produced.")
                    
                with open(log_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(log_lines))
                    
                print(f" {status}")
                
        print("\n" + "=" * 60)
        print("Simulation Run Summary:")
        print(f"  Total Scripts Executed: {total_scripts}")
        print(f"  Successful: {successful_runs}")
        print(f"  Failed: {failed_runs}")
        print(f"  Timed out (Interactive): {timeout_runs}")
        print("=" * 60)
        
    finally:
        # Clean up temp runner directory
        if temp_runner_dir.exists():
            shutil.rmtree(temp_runner_dir)

if __name__ == "__main__":
    main()
