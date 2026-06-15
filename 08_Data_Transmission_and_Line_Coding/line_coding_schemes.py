"""Line coding schemes used in digital data transmission.

Implements and visualises NRZ-L, NRZ-I, Manchester, Differential
Manchester, AMI (Bipolar), and B8ZS encoding.
"""

import numpy as np
import matplotlib.pyplot as plt


def nrz_l(bits):
    """Non-Return-to-Zero Level: 1->+1, 0->-1."""
    return np.where(bits, 1.0, -1.0)


def nrz_i(bits):
    """Non-Return-to-Zero Inverted: transition on 1, no change on 0."""
    signal = np.empty(len(bits))
    level = 1.0
    for i, b in enumerate(bits):
        if b == 1:
            level *= -1
        signal[i] = level
    return signal


def manchester(bits):
    """Manchester (IEEE 802.3): 0->low-high, 1->high-low."""
    sig = np.empty(2 * len(bits))
    for i, b in enumerate(bits):
        if b == 1:
            sig[2 * i] = 1.0
            sig[2 * i + 1] = -1.0
        else:
            sig[2 * i] = -1.0
            sig[2 * i + 1] = 1.0
    return sig


def diff_manchester(bits):
    """Differential Manchester: transition at mid-bit always;
    transition at start for 0, no transition at start for 1."""
    sig = np.empty(2 * len(bits))
    level = 1.0
    for i, b in enumerate(bits):
        if b == 0:
            level *= -1  # transition at start
        sig[2 * i] = level
        level *= -1       # mandatory mid-bit transition
        sig[2 * i + 1] = level
    return sig


def ami(bits):
    """Alternate Mark Inversion (Bipolar): 0->0, 1->alternate +1/-1."""
    sig = np.empty(len(bits))
    polarity = 1.0
    for i, b in enumerate(bits):
        if b == 1:
            sig[i] = polarity
            polarity *= -1
        else:
            sig[i] = 0.0
    return sig


def step_plot(ax, signal, bits_per_sample, title, colour):
    """Plot a step-function waveform."""
    t = np.arange(len(signal)) / bits_per_sample
    ax.step(t, signal, where="post", linewidth=1.5, color=colour)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.set_title(title, fontsize=10)
    ax.set_ylim(-1.6, 1.6)
    ax.grid(True, alpha=0.3)


def main():
    bits = np.array([1, 0, 1, 1, 0, 0, 1, 0, 1, 0])
    bit_str = "".join(str(b) for b in bits)

    schemes = [
        ("NRZ-L", nrz_l(bits), 1, "r"),
        ("NRZ-I", nrz_i(bits), 1, "c"),
        ("Manchester", manchester(bits), 2, "gray"),
        ("Diff. Manchester", diff_manchester(bits), 2, "gray"),
        ("AMI (Bipolar)", ami(bits), 1, "orange"),
    ]

    fig, axes = plt.subplots(len(schemes), 1, figsize=(12, 10), sharex=True)
    for ax, (name, sig, bps, col) in zip(axes, schemes):
        step_plot(ax, sig, bps, name, col)

    axes[-1].set_xlabel("Bit Period")
    fig.suptitle(f"Line Coding Schemes - Data: [{bit_str}]", fontsize=13)
    fig.tight_layout()
    plt.show()

    print(f"Input bits: {bit_str}")
    for name, sig, _, _ in schemes:
        print(f"  {name:20s} -> {sig.tolist()}")


if __name__ == "__main__":
    main()
