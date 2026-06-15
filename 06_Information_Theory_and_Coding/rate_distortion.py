"""Rate-Distortion Functions for Gaussian and Binary Sources.

Plots the theoretical rate-distortion curves R(D) representing the lower bound
on rate required for a given distortion level under lossy compression.
"""

import numpy as np
import matplotlib.pyplot as plt


def binary_entropy(p):
    """Compute binary entropy H(p)."""
    p = np.clip(p, 1e-12, 1.0 - 1e-12)
    return -p * np.log2(p) - (1.0 - p) * np.log2(1.0 - p)


def gaussian_rate_distortion(d, sigma_sq):
    """Calculate R(D) for a Gaussian source with variance sigma_sq under MSE distortion."""
    d = np.atleast_1d(d)
    rate = np.zeros_like(d)
    mask = (d > 0) & (d < sigma_sq)
    rate[mask] = 0.5 * np.log2(sigma_sq / d[mask])
    return rate


def binary_rate_distortion(d):
    """Calculate R(D) for a Bernoulli(0.5) source under Hamming distortion."""
    d = np.atleast_1d(d)
    rate = np.zeros_like(d)
    mask = (d > 0) & (d < 0.5)
    rate[mask] = 1.0 - binary_entropy(d[mask])
    return rate


def main():
    # --- Gaussian Source R(D) ---
    distortions_gauss = np.linspace(0.001, 5.0, 500)
    variances = [1.0, 2.0, 4.0]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    colors = ["c", "gray", "r"]
    for var, col in zip(variances, colors):
        r_d = gaussian_rate_distortion(distortions_gauss, var)
        ax1.plot(distortions_gauss, r_d, label=f"Gaussian Source (rho^2 = {var:.1f})", color=col, linewidth=2)
        # Mark Shannon limit: at D=sigma_sq, R(D) becomes 0
        ax1.plot(var, 0.0, "o", color=col, markersize=6)
        ax1.text(var, 0.1, f" D=rho^2={var}", fontsize=9, verticalalignment="bottom")

    ax1.set_title("Gaussian Source Rate-Distortion Function (MSE Distortion)", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Distortion D (Mean Squared Error)")
    ax1.set_ylabel("Rate R(D) (bits per sample)")
    ax1.set_xlim(0, 5.0)
    ax1.set_ylim(-0.1, 2.5)
    ax1.grid(True, linestyle="--", alpha=0.5)
    ax1.legend()

    # --- Binary Source R(D) ---
    distortions_bin = np.linspace(0.0, 0.6, 500)
    r_d_bin = binary_rate_distortion(distortions_bin)

    ax2.plot(distortions_bin, r_d_bin, label="Binary Source (p = 0.5)", color="gray", linewidth=2.5)
    ax2.plot(0.5, 0.0, "ko", markersize=6)
    ax2.text(0.5, 0.05, " D=p=0.5", fontsize=10, verticalalignment="bottom")

    ax2.set_title("Binary Source Rate-Distortion Function (Hamming Distortion)", fontsize=12, fontweight="bold")
    ax2.set_xlabel("Distortion D (Hamming Error Probability)")
    ax2.set_ylabel("Rate R(D) (bits per sample)")
    ax2.set_xlim(0, 0.6)
    ax2.set_ylim(-0.05, 1.1)
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.legend()

    plt.suptitle("Rate-Distortion Theory: Bounds on Lossy Source Coding", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

    # Output explanation
    print("=== Rate-Distortion Theory Insights ===")
    print("1. For distortion D >= rho^2 (for Gaussian) or D >= 0.5 (for Binary), the required rate R(D) is 0.")
    print("   This means we can achieve that level of distortion by transmitting nothing (just guessing the mean).")
    print("2. As distortion D approaches 0 (lossless transmission), the required rate goes to infinity for continuous")
    print("   sources (Gaussian) and approaches the source entropy (H(X)=1 bit) for the binary source.")


if __name__ == "__main__":
    main()
