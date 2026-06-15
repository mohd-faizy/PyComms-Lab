"""Probability distributions used in communication engineering.

Plots Uniform, Exponential, Rayleigh, and Rician distributions that
frequently appear in fading channel models and noise analysis.  Prints
mean, variance, and higher moments for each.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, expon, rayleigh, rice


def main():
    x = np.linspace(0, 8, 500)

    distributions = [
        ("Uniform(0,4)", uniform(loc=0, scale=4)),
        ("Exponential(lambda=1)", expon(scale=1)),
        ("Rayleigh(rho=1)", rayleigh(scale=1)),
        ("Rician(nu=2, rho=1)", rice(b=2, scale=1)),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.ravel()

    colours = ["c", "r", "gray", "gray"]

    for ax, (name, dist), colour in zip(axes, distributions, colours):
        pdf = dist.pdf(x)
        cdf = dist.cdf(x)
        ax.plot(x, pdf, color=colour, lw=2, label="PDF")
        ax.fill_between(x, pdf, alpha=0.2, color=colour)
        ax2 = ax.twinx()
        ax2.plot(x, cdf, "--", color="grey", lw=1.5, label="CDF")
        ax2.set_ylim(0, 1.15)
        ax2.set_ylabel("CDF")

        ax.set_title(name, fontsize=11, fontweight="bold")
        ax.set_xlabel("x")
        ax.set_ylabel("PDF")
        ax.grid(True, alpha=0.3)
        ax.legend(loc="upper left", fontsize=8)
        ax2.legend(loc="upper right", fontsize=8)

    fig.suptitle("Probability Distributions in Communication Systems", fontsize=13)
    fig.tight_layout()
    plt.show()

    print("=" * 60)
    print(f"{'Distribution':<25} {'Mean':>8} {'Var':>8} {'Skew':>8} {'Kurt':>8}")
    print("-" * 60)
    for name, dist in distributions:
        m, v, s, k = dist.stats(moments="mvsk")
        print(f"{name:<25} {float(m):8.4f} {float(v):8.4f} {float(s):8.4f} {float(k):8.4f}")


if __name__ == "__main__":
    main()
