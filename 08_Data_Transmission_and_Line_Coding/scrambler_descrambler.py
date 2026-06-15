"""Scrambler and descrambler for digital data transmission.

Demonstrates additive (synchronous) scrambling used in data communication
to ensure sufficient transitions and remove long runs of 0s or 1s.  Shows
the effect on the data power spectrum.
"""

import numpy as np
import matplotlib.pyplot as plt


def lfsr_step(register, taps):
    """Single step of a Linear Feedback Shift Register."""
    feedback = 0
    for tap in taps:
        feedback ^= register[tap]
    register = np.roll(register, 1)
    register[0] = feedback
    return register, feedback


def additive_scrambler(data, poly_taps, seed):
    """Additive scrambler: output = data XOR LFSR output."""
    reg = seed.copy()
    scrambled = np.zeros_like(data)
    for i in range(len(data)):
        reg, fb = lfsr_step(reg, poly_taps)
        scrambled[i] = data[i] ^ fb
    return scrambled


def additive_descrambler(data, poly_taps, seed):
    """Additive descrambler (identical to scrambler for additive type)."""
    return additive_scrambler(data, poly_taps, seed)


def plot_psd(ax, data, title, colour):
    """Plot the power spectral density of a binary sequence."""
    signal = 2.0 * data.astype(float) - 1.0
    n = len(signal)
    psd = np.abs(np.fft.rfft(signal)) ** 2 / n
    freqs = np.fft.rfftfreq(n)
    ax.semilogy(freqs, psd, color=colour, alpha=0.7)
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("Normalised Frequency")
    ax.set_ylabel("PSD")
    ax.grid(True, alpha=0.3)


def main():
    rng = np.random.default_rng(77)
    n = 4096

    # Pathological data: long runs of zeros
    data_bad = np.zeros(n, dtype=int)
    data_bad[:100] = 1
    # Random data (for comparison)
    data_rand = rng.integers(0, 2, n)

    # LFSR config: x^7 + x^6 + 1 (taps at positions 6 and 5, zero-indexed)
    poly_taps = [5, 6]
    seed = np.array([1, 0, 0, 1, 0, 1, 1], dtype=int)

    scrambled_bad = additive_scrambler(data_bad, poly_taps, seed.copy())
    descrambled = additive_descrambler(scrambled_bad, poly_taps, seed.copy())

    # Verify correctness
    assert np.array_equal(data_bad, descrambled), "Descrambler mismatch!"

    scrambled_rand = additive_scrambler(data_rand, poly_taps, seed.copy())

    fig, axes = plt.subplots(2, 3, figsize=(15, 7))

    # Time-domain waveforms
    show = 200
    axes[0, 0].step(range(show), data_bad[:show], where="post", color="tab:red")
    axes[0, 0].set_title("Original (long zeros)")
    axes[0, 0].set_ylim(-0.3, 1.3)
    axes[0, 0].grid(True, alpha=0.3)

    axes[0, 1].step(range(show), scrambled_bad[:show], where="post",
                    color="tab:blue")
    axes[0, 1].set_title("After Scrambling")
    axes[0, 1].set_ylim(-0.3, 1.3)
    axes[0, 1].grid(True, alpha=0.3)

    axes[0, 2].step(range(show), descrambled[:show], where="post",
                    color="tab:green")
    axes[0, 2].set_title("Descrambled (recovered)")
    axes[0, 2].set_ylim(-0.3, 1.3)
    axes[0, 2].grid(True, alpha=0.3)

    # PSDs
    plot_psd(axes[1, 0], data_bad, "PSD - Original (pathological)", "tab:red")
    plot_psd(axes[1, 1], scrambled_bad, "PSD - Scrambled", "tab:blue")
    plot_psd(axes[1, 2], data_rand, "PSD - Random data (ideal)", "tab:green")

    fig.suptitle("Additive Scrambler / Descrambler", fontsize=13)
    fig.tight_layout()
    plt.show()

    print("Scrambling whitens the spectrum, ensuring clock recovery is reliable.")
    print(f"Verified: descrambled == original? {np.array_equal(data_bad, descrambled)}")


if __name__ == "__main__":
    main()
