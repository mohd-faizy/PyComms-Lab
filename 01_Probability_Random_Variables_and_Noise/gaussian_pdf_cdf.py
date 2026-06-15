"""Gaussian PDF and CDF visualization.

Plots the probability density function and cumulative distribution function
of the Gaussian (normal) distribution for different mean and standard
deviation values.  This is foundational to noise analysis in communication
systems.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def main():
    x = np.linspace(-10, 10, 1000)

    params = [
        (0, 1, "mu=0, rho=1"),
        (0, 2, "mu=0, rho=2"),
        (0, 0.5, "mu=0, rho=0.5"),
        (2, 1, "mu=2, rho=1"),
        (-2, 1.5, "mu=-2, rho=1.5"),
    ]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # --- PDF ---
    for mu, sigma, label in params:
        axes[0].plot(x, norm.pdf(x, mu, sigma), label=label)
    axes[0].set_title("Gaussian Probability Density Function (PDF)")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("f(x)")
    axes[0].legend()
    axes[0].grid(True)

    # --- CDF ---
    for mu, sigma, label in params:
        axes[1].plot(x, norm.cdf(x, mu, sigma), label=label)
    axes[1].set_title("Gaussian Cumulative Distribution Function (CDF)")
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("F(x)")
    axes[1].legend()
    axes[1].grid(True)

    fig.suptitle("Gaussian Distribution - Foundation of AWGN Noise", fontsize=13)
    fig.tight_layout()
    plt.show()

    # Print key probabilities
    print("=== Standard Normal Distribution (mu=0, rho=1) ===")
    for k in [1, 2, 3]:
        p = norm.cdf(k) - norm.cdf(-k)
        print(f"  P(-{k}rho < X < {k}rho) = {p:.6f}  ({p*100:.2f}%)")


if __name__ == "__main__":
    main()
