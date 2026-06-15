"""ARQ (Automatic Repeat reQuest) protocol simulation.

Simulates Stop-and-Wait, Go-Back-N, and Selective Repeat ARQ protocols
over a lossy link and compares their throughput efficiency.
"""

import numpy as np
import matplotlib.pyplot as plt


def stop_and_wait(n_frames, per, rng):
    """Stop-and-Wait ARQ: send one frame, wait for ACK."""
    transmissions = 0
    for _ in range(n_frames):
        while True:
            transmissions += 1
            if rng.random() > per:
                break  # ACK received
    return transmissions


def go_back_n(n_frames, per, window_size, rng):
    """Go-Back-N ARQ: retransmit from the failed frame."""
    transmissions = 0
    next_to_send = 0
    while next_to_send < n_frames:
        # Send a window of frames
        sent_count = min(window_size, n_frames - next_to_send)
        first_fail = -1
        for i in range(sent_count):
            transmissions += 1
            if rng.random() < per and first_fail == -1:
                first_fail = i
        if first_fail == -1:
            next_to_send += sent_count  # all OK
        else:
            next_to_send += first_fail  # go back to failed frame
    return transmissions


def selective_repeat(n_frames, per, window_size, rng):
    """Selective Repeat ARQ: retransmit only failed frames."""
    transmissions = 0
    acked = np.zeros(n_frames, dtype=bool)
    while not np.all(acked):
        # Find frames to send (up to window_size unacked frames)
        to_send = np.where(~acked)[0][:window_size]
        for idx in to_send:
            transmissions += 1
            if rng.random() > per:
                acked[idx] = True
    return transmissions


def main():
    rng = np.random.default_rng(42)
    n_frames = 500
    window_size = 8
    per_values = np.arange(0.0, 0.55, 0.05)
    n_trials = 20

    results = {
        "Stop-and-Wait": [],
        "Go-Back-N (W=8)": [],
        "Selective Repeat (W=8)": [],
    }

    for per in per_values:
        saw_eff, gbn_eff, sr_eff = [], [], []
        for _ in range(n_trials):
            saw = stop_and_wait(n_frames, per, rng)
            gbn = go_back_n(n_frames, per, window_size, rng)
            sr = selective_repeat(n_frames, per, window_size, rng)
            saw_eff.append(n_frames / saw)
            gbn_eff.append(n_frames / gbn)
            sr_eff.append(n_frames / sr)
        results["Stop-and-Wait"].append(np.mean(saw_eff))
        results["Go-Back-N (W=8)"].append(np.mean(gbn_eff))
        results["Selective Repeat (W=8)"].append(np.mean(sr_eff))

    fig, ax = plt.subplots(figsize=(10, 6))
    colours = {"Stop-and-Wait": "tab:red", "Go-Back-N (W=8)": "tab:blue",
               "Selective Repeat (W=8)": "tab:green"}
    for name, eff_list in results.items():
        ax.plot(per_values * 100, eff_list, "o-", label=name,
                color=colours[name], markersize=5)

    ax.set_title("ARQ Protocol Throughput Efficiency", fontsize=13)
    ax.set_xlabel("Frame Error Rate (%)")
    ax.set_ylabel("Throughput Efficiency (delivered / transmitted)")
    ax.set_ylim(0, 1.05)
    ax.legend()
    ax.grid(True)
    fig.tight_layout()
    plt.show()

    print("=== Throughput at 10% FER ===")
    idx = 2  # 10%
    for name, eff_list in results.items():
        print(f"  {name:30s}: {eff_list[idx]:.3f}")


if __name__ == "__main__":
    main()
