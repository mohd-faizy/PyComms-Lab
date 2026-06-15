"""PN (Pseudo-Noise) sequence generator using LFSR.

Implements a Linear Feedback Shift Register to generate maximal-length
(m-sequence) PN codes.  Plots the sequence and its autocorrelation to
demonstrate the near-ideal 'thumb-tack' autocorrelation property.
"""

import numpy as np
import matplotlib.pyplot as plt


def lfsr_m_sequence(n_bits, taps, seed=None):
    """Generate a maximal-length sequence using an LFSR.

    Parameters
    ----------
    n_bits : int   - Register length
    taps : list    - Feedback tap positions (0-indexed)
    seed : list    - Initial register state (default: all ones)

    Returns
    -------
    sequence : ndarray of +/-1 values, length 2^n_bits - 1
    """
    period = 2 ** n_bits - 1
    if seed is None:
        reg = np.ones(n_bits, dtype=int)
    else:
        reg = np.array(seed, dtype=int)

    seq = np.empty(period, dtype=int)
    for i in range(period):
        seq[i] = reg[-1]  # output bit
        feedback = 0
        for tap in taps:
            feedback ^= reg[tap]
        reg = np.roll(reg, 1)
        reg[0] = feedback

    # Map {0,1} -> {-1,+1}
    return 2 * seq - 1


def circular_autocorrelation(seq):
    """Compute normalised circular autocorrelation."""
    n = len(seq)
    acf = np.empty(n)
    for lag in range(n):
        acf[lag] = np.sum(seq * np.roll(seq, lag)) / n
    return acf


def main():
    # LFSR configurations for different register lengths
    configs = [
        (4, [0, 3], "4-bit LFSR (period 15)"),
        (5, [1, 4], "5-bit LFSR (period 31)"),
        (7, [0, 6], "7-bit LFSR (period 127)"),
    ]

    fig, axes = plt.subplots(len(configs), 2, figsize=(14, 3.5 * len(configs)))

    for i, (n, taps, title) in enumerate(configs):
        seq = lfsr_m_sequence(n, taps)
        acf = circular_autocorrelation(seq)
        period = len(seq)

        # Sequence
        axes[i, 0].step(range(period), seq, where="post", lw=0.8,
                       color="tab:blue")
        axes[i, 0].set_title(f"{title} - m-sequence")
        axes[i, 0].set_ylim(-1.5, 1.5)
        axes[i, 0].set_xlabel("Chip index")
        axes[i, 0].grid(True, alpha=0.3)

        # Autocorrelation
        axes[i, 1].stem(range(period), acf, linefmt="tab:orange",
                       markerfmt=".", basefmt="k-")
        axes[i, 1].set_title(f"Circular Autocorrelation (peak = 1, off-peak ~ -1/{period})")
        axes[i, 1].set_xlabel("Lag (chips)")
        axes[i, 1].grid(True, alpha=0.3)

    fig.suptitle("PN Sequence Generation - LFSR m-Sequences", fontsize=13)
    fig.tight_layout()
    plt.show()

    for n, taps, title in configs:
        seq = lfsr_m_sequence(n, taps)
        acf = circular_autocorrelation(seq)
        print(f"{title}: period={len(seq)}, "
              f"autocorrelation peak=1.0, "
              f"off-peak={acf[1]:.4f}")


if __name__ == "__main__":
    main()
