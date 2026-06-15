"""Central Limit Theorem demonstration.

Shows that the sum of many independent random variables (uniform or
exponential) converges to a Gaussian distribution regardless of the
original distribution.  This explains why thermal noise is modelled as
Gaussian.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def demonstrate_clt(rng, dist_name, sampler, n_trials=50000):
    """Sum increasing numbers of RVs and plot the resulting distribution."""
    counts = [1, 2, 5, 10, 30]
    fig, axes = plt.subplots(1, len(counts), figsize=(16, 3.5))

    for ax, n in zip(axes, counts):
        samples = sampler(rng, size=(n_trials, n))
        sums = samples.sum(axis=1)
        # Standardise
        sums = (sums - sums.mean()) / sums.std()

        ax.hist(sums, bins=60, density=True, alpha=0.7, color="steelblue",
                edgecolor="white", linewidth=0.3)
        x = np.linspace(-4, 4, 200)
        ax.plot(x, norm.pdf(x), "r-", lw=2, label="N(0,1)")
        ax.set_title(f"N = {n}")
        ax.set_xlim(-4, 4)
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

    fig.suptitle(f"CLT with {dist_name} Distribution", fontsize=13)
    fig.tight_layout()
    return fig


def main():
    rng = np.random.default_rng(99)

    # Uniform [0, 1]
    demonstrate_clt(rng, "Uniform(0,1)",
                    lambda r, size: r.uniform(0, 1, size=size))

    # Exponential lambda=1
    demonstrate_clt(rng, "Exponential(lambda=1)",
                    lambda r, size: r.exponential(1, size=size))

    plt.show()

    print("As N increases, the distribution of the sum approaches Gaussian.")
    print("This is why aggregated noise sources in receivers are modelled as AWGN.")


if __name__ == "__main__":
    main()
