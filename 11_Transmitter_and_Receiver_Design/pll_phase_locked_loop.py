"""Phase-Locked Loop (PLL) simulation.

Simulates a basic PLL consisting of a phase detector, loop filter, and VCO.
Demonstrates frequency acquisition (lock-in) behavior and phase tracking.
"""

import numpy as np
import matplotlib.pyplot as plt


def simulate_pll(f_input, f_vco_free, fs, n_samples, kp=0.01, ki=0.005):
    """Simulate a digital PLL tracking a sinusoidal input.

    Parameters
    ----------
    f_input : float   - Input signal frequency (Hz)
    f_vco_free : float - VCO free-running frequency (Hz)
    fs : float         - Sampling frequency (Hz)
    n_samples : int    - Number of samples
    kp, ki : float     - Proportional and integral loop-filter gains
    """
    t = np.arange(n_samples) / fs
    input_signal = np.sin(2 * np.pi * f_input * t)

    phase_vco = 0.0
    freq_vco = f_vco_free
    integrator = 0.0

    vco_output = np.empty(n_samples)
    phase_error = np.empty(n_samples)
    vco_freq_log = np.empty(n_samples)

    for i in range(n_samples):
        # VCO output
        vco_output[i] = np.cos(phase_vco)

        # Phase detector (multiplier type)
        pd_out = input_signal[i] * vco_output[i]

        # Loop filter (PI controller)
        integrator += ki * pd_out
        loop_out = kp * pd_out + integrator

        # VCO update
        freq_vco = f_vco_free + loop_out * fs
        phase_vco += 2 * np.pi * freq_vco / fs

        phase_error[i] = pd_out
        vco_freq_log[i] = freq_vco

    return t, input_signal, vco_output, phase_error, vco_freq_log


def main():
    fs = 10_000
    n = 5000
    f_input = 200
    f_vco_free = 180  # start off-frequency

    t, inp, vco, pe, vco_f = simulate_pll(f_input, f_vco_free, fs, n)

    fig, axes = plt.subplots(4, 1, figsize=(12, 10), sharex=True)

    axes[0].plot(t, inp, lw=0.7, label="Input")
    axes[0].set_title("Input Signal")
    axes[0].grid(True)
    axes[0].legend()

    axes[1].plot(t, vco, lw=0.7, color="tab:orange", label="VCO output")
    axes[1].set_title("VCO Output")
    axes[1].grid(True)
    axes[1].legend()

    axes[2].plot(t, pe, lw=0.7, color="tab:green")
    axes[2].set_title("Phase Error (PD Output)")
    axes[2].grid(True)

    axes[3].plot(t, vco_f, lw=1.0, color="tab:red")
    axes[3].axhline(f_input, ls="--", color="k", lw=0.8, label=f"Target {f_input} Hz")
    axes[3].set_title("VCO Frequency (Hz)")
    axes[3].set_xlabel("Time (s)")
    axes[3].legend()
    axes[3].grid(True)

    fig.suptitle(f"PLL Simulation - Locking from {f_vco_free} Hz to {f_input} Hz",
                 fontsize=13)
    fig.tight_layout()
    plt.show()

    print(f"Input frequency    : {f_input} Hz")
    print(f"VCO free-run freq  : {f_vco_free} Hz")
    print(f"Final VCO frequency: {vco_f[-1]:.2f} Hz")
    print(f"Lock achieved      : {'Yes' if abs(vco_f[-1] - f_input) < 2 else 'No'}")


if __name__ == "__main__":
    main()
