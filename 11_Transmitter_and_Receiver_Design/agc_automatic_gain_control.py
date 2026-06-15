"""Automatic Gain Control (AGC) simulation.

Simulates an AGC loop that stabilizes the output level of a receiver
when the input signal amplitude varies over time.
"""

import numpy as np
import matplotlib.pyplot as plt


def agc_loop(signal, target_level=1.0, attack=0.01, decay=0.001):
    """Simple feedback AGC loop.

    Parameters
    ----------
    signal : array - Input signal with varying amplitude
    target_level : float - Desired RMS output level
    attack : float - Gain-decrease speed (fast attack)
    decay : float  - Gain-increase speed (slow decay)
    """
    n = len(signal)
    output = np.empty(n)
    gain = np.empty(n)
    g = 1.0

    for i in range(n):
        output[i] = g * signal[i]
        error = target_level - abs(output[i])
        if error < 0:
            g += attack * error  # decrease gain quickly
        else:
            g += decay * error   # increase gain slowly
        g = max(g, 0.01)        # prevent zero/negative gain
        gain[i] = g

    return output, gain


def main():
    fs = 10_000
    t = np.arange(0, 2, 1 / fs)

    # Simulate a carrier with time-varying amplitude (fading envelope)
    carrier = np.sin(2 * np.pi * 200 * t)
    envelope = 0.3 + 0.7 * np.abs(np.sin(2 * np.pi * 0.8 * t))
    # Add step changes
    envelope[5000:8000] *= 3.0
    envelope[12000:15000] *= 0.3

    rx_signal = envelope * carrier

    output, gain = agc_loop(rx_signal, target_level=1.0)

    fig, axes = plt.subplots(3, 1, figsize=(13, 8), sharex=True)

    axes[0].plot(t, rx_signal, lw=0.5, color="tab:blue")
    axes[0].plot(t, envelope, "r-", lw=1.5, label="Envelope")
    axes[0].set_title("Input Signal (varying amplitude)")
    axes[0].legend()
    axes[0].grid(True)

    axes[1].plot(t, output, lw=0.5, color="tab:green")
    axes[1].axhline(1.0, ls="--", color="red", lw=0.8, label="Target")
    axes[1].axhline(-1.0, ls="--", color="red", lw=0.8)
    axes[1].set_title("AGC Output (stabilised)")
    axes[1].legend()
    axes[1].grid(True)

    axes[2].plot(t, gain, lw=1.2, color="tab:orange")
    axes[2].set_title("AGC Gain (dB-like)")
    axes[2].set_xlabel("Time (s)")
    axes[2].grid(True)

    fig.suptitle("Automatic Gain Control (AGC) - Receiver Gain Stabilisation",
                 fontsize=13)
    fig.tight_layout()
    plt.show()

    print(f"Input amplitude range : {np.abs(rx_signal).min():.3f} - "
          f"{np.abs(rx_signal).max():.3f}")
    print(f"Output amplitude range: {np.abs(output[1000:]).min():.3f} - "
          f"{np.abs(output[1000:]).max():.3f}")


if __name__ == "__main__":
    main()
