"""Inter-Symbol Interference (ISI) and pulse shaping.

Demonstrates the Nyquist criterion for zero-ISI and shows how raised-cosine
filtering eliminates ISI at optimal sampling instants.
"""

import numpy as np
import matplotlib.pyplot as plt


def raised_cosine(t, T, beta):
    """Raised-cosine pulse shape p(t)."""
    p = np.zeros_like(t)
    for i, ti in enumerate(t):
        x = ti / T
        if abs(ti) < 1e-12:
            p[i] = 1.0
        elif abs(abs(2 * beta * x) - 1) < 1e-12:
            p[i] = (np.pi / (4 * T)) * np.sinc(1 / (2 * beta))
        else:
            p[i] = np.sinc(x) * np.cos(np.pi * beta * x) / (1 - (2 * beta * x) ** 2)
    return p


def main():
    T = 1.0  # symbol period
    t = np.linspace(-6 * T, 6 * T, 2000)
    betas = [0.0, 0.25, 0.5, 0.75, 1.0]

    # --- Part 1: Raised-cosine pulses for different roll-off factors ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    for beta in betas:
        p = raised_cosine(t, T, beta)
        axes[0].plot(t, p, label=f"beta = {beta}")

    axes[0].set_title("Raised-Cosine Pulse p(t)")
    axes[0].set_xlabel("Time / T")
    axes[0].set_ylabel("Amplitude")
    axes[0].axhline(0, color="k", lw=0.5)
    axes[0].legend()
    axes[0].grid(True)

    # Frequency response
    for beta in betas:
        p = raised_cosine(t, T, beta)
        freqs = np.fft.rfftfreq(len(t), t[1] - t[0])
        H = np.abs(np.fft.rfft(p))
        H /= H.max()
        axes[1].plot(freqs, H, label=f"beta = {beta}")

    axes[1].set_xlim(0, 1.5 / T)
    axes[1].set_title("Raised-Cosine Frequency Response |H(f)|")
    axes[1].set_xlabel("Frequency (1/T)")
    axes[1].set_ylabel("Magnitude")
    axes[1].legend()
    axes[1].grid(True)

    fig.suptitle("ISI-Free Pulse Shaping - Nyquist Criterion", fontsize=13)
    fig.tight_layout()

    # --- Part 2: ISI demonstration ---
    rng = np.random.default_rng(42)
    n_sym = 10
    symbols = 2 * rng.integers(0, 2, n_sym) - 1  # +/-1

    fig2, axes2 = plt.subplots(1, 2, figsize=(14, 5))

    for ax, beta, title in zip(axes2, [0.0, 0.5],
                                ["beta=0 (sinc - heavy ISI tails)",
                                 "beta=0.5 (moderate roll-off)"]):
        t_full = np.linspace(-2 * T, (n_sym + 2) * T, 3000)
        composite = np.zeros_like(t_full)
        for k, a in enumerate(symbols):
            composite += a * raised_cosine(t_full - k * T, T, beta)
            ax.plot(t_full, a * raised_cosine(t_full - k * T, T, beta),
                    alpha=0.3, lw=0.8)
        ax.plot(t_full, composite, "k-", lw=2, label="Composite")
        # Mark sampling instants
        for k, a in enumerate(symbols):
            ax.plot(k * T, a, "ro", markersize=6)
        ax.set_title(title)
        ax.set_xlabel("Time / T")
        ax.legend()
        ax.grid(True)

    fig2.suptitle("ISI: Individual Pulses and Composite Signal", fontsize=13)
    fig2.tight_layout()
    plt.show()

    print("At optimal sampling instants (red dots), the Nyquist criterion")
    print("guarantees zero ISI from neighbouring symbols.")


if __name__ == "__main__":
    main()
