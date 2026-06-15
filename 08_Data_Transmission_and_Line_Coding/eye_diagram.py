"""Eye diagram generation for baseband digital transmission.

Generates eye diagrams for rectangular and raised-cosine pulse shapes,
showing the effect of ISI and noise on the 'eye opening'.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter


def raised_cosine_filter(beta, span, sps):
    """Design a raised-cosine FIR filter."""
    n = np.arange(-span * sps // 2, span * sps // 2 + 1)
    t = n / sps
    h = np.sinc(t)
    denom = 1 - (2 * beta * t) ** 2
    # Handle singularities
    denom[np.abs(denom) < 1e-12] = 1e-12
    h *= np.cos(np.pi * beta * t) / denom
    return h / np.sum(h)


def generate_eye(bits, sps, pulse_filter, snr_db, rng):
    """Generate the signal for an eye diagram."""
    symbols = 2.0 * bits - 1.0  # map {0,1} -> {-1,+1}
    # Upsample
    up = np.zeros(len(symbols) * sps)
    up[::sps] = symbols
    # Pulse shape
    tx = np.convolve(up, pulse_filter, mode="same")
    # Add AWGN
    sig_power = np.mean(tx ** 2)
    noise_power = sig_power / (10 ** (snr_db / 10))
    rx = tx + rng.normal(scale=np.sqrt(noise_power), size=tx.size)
    return rx


def plot_eye(ax, signal, sps, title):
    """Overlay 2-symbol-wide traces to form an eye diagram."""
    trace_len = 2 * sps
    n_traces = len(signal) // trace_len - 1
    for i in range(n_traces):
        seg = signal[i * trace_len: (i + 1) * trace_len]
        ax.plot(np.linspace(0, 2, trace_len), seg, color="steelblue",
                alpha=0.15, linewidth=0.5)
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("Symbol Period")
    ax.set_ylabel("Amplitude")
    ax.grid(True, alpha=0.3)


def main():
    rng = np.random.default_rng(123)
    n_bits = 2000
    sps = 16  # samples per symbol
    bits = rng.integers(0, 2, n_bits)

    # Rectangular pulse
    rect_pulse = np.ones(sps)
    rect_pulse /= np.sum(rect_pulse)

    # Raised cosine (roll-off = 0.35)
    rc_pulse = raised_cosine_filter(beta=0.35, span=6, sps=sps)

    snr_values = [20, 10]

    fig, axes = plt.subplots(2, 2, figsize=(13, 8))

    for col, snr in enumerate(snr_values):
        rx_rect = generate_eye(bits, sps, rect_pulse, snr, rng)
        rx_rc = generate_eye(bits, sps, rc_pulse, snr, rng)

        plot_eye(axes[0, col], rx_rect, sps,
                 f"Rectangular Pulse - SNR={snr} dB")
        plot_eye(axes[1, col], rx_rc, sps,
                 f"Raised Cosine (beta=0.35) - SNR={snr} dB")

    fig.suptitle("Eye Diagrams - Effect of Pulse Shape and Noise", fontsize=13)
    fig.tight_layout()
    plt.show()

    print("A wider 'eye opening' indicates less ISI and better noise margin.")


if __name__ == "__main__":
    main()
