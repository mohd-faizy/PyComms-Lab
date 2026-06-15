"""Direct-conversion (zero-IF) receiver simulation.

Demonstrates I/Q demodulation where the RF signal is mixed directly to
baseband.  Compares with the superheterodyne approach.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfiltfilt


def lowpass(x, cutoff, fs, order=5):
    sos = butter(order, cutoff, fs=fs, output="sos")
    return sosfiltfilt(sos, x)


def main():
    fs = 500_000
    t = np.arange(0, 0.005, 1 / fs)
    fc = 50_000  # carrier
    fm = 2_000   # message frequency

    # Transmitted AM signal
    message = np.cos(2 * np.pi * fm * t)
    tx = (1 + 0.5 * message) * np.cos(2 * np.pi * fc * t)

    # === Direct-Conversion Receiver ===
    # Local oscillator at exactly fc
    lo_i = 2 * np.cos(2 * np.pi * fc * t)   # in-phase
    lo_q = -2 * np.sin(2 * np.pi * fc * t)  # quadrature

    # Mix to baseband
    i_raw = tx * lo_i
    q_raw = tx * lo_q

    # Low-pass filter to remove 2fc component
    i_bb = lowpass(i_raw, 10_000, fs)
    q_bb = lowpass(q_raw, 10_000, fs)

    # Envelope
    envelope = np.sqrt(i_bb ** 2 + q_bb ** 2)

    fig, axes = plt.subplots(4, 1, figsize=(13, 10), sharex=True)

    axes[0].plot(t * 1000, tx, lw=0.4, color="tab:blue")
    axes[0].set_title("Received RF Signal (AM)")
    axes[0].grid(True)

    axes[1].plot(t * 1000, i_bb, label="I (In-phase)", lw=0.8)
    axes[1].plot(t * 1000, q_bb, label="Q (Quadrature)", lw=0.8)
    axes[1].set_title("Baseband I/Q Components")
    axes[1].legend()
    axes[1].grid(True)

    axes[2].plot(t * 1000, envelope, color="tab:green", lw=1.2, label="Envelope")
    axes[2].set_title("Recovered Envelope (demodulated)")
    axes[2].legend()
    axes[2].grid(True)

    axes[3].plot(t * 1000, message, "r-", lw=1.5, label="Original message")
    axes[3].plot(t * 1000, envelope - np.mean(envelope), "--",
                color="tab:green", lw=1.2, label="Recovered (DC removed)")
    axes[3].set_title("Comparison: Original vs Recovered")
    axes[3].set_xlabel("Time (ms)")
    axes[3].legend()
    axes[3].grid(True)

    fig.suptitle("Direct-Conversion (Zero-IF) Receiver - I/Q Demodulation",
                 fontsize=13)
    fig.tight_layout()
    plt.show()

    print("Direct-conversion receiver converts RF directly to baseband.")
    print("Advantages: simpler architecture, no image frequency problem.")
    print("Disadvantages: DC offset, I/Q imbalance, flicker noise.")


if __name__ == "__main__":
    main()
