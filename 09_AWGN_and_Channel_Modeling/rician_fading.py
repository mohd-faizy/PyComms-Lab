import numpy as np
import matplotlib.pyplot as plt


def rician_fading(k_factor, samples, rng):
    los = np.sqrt(k_factor / (k_factor + 1))
    scatter = np.sqrt(1 / (k_factor + 1)) * (
        rng.normal(size=samples) + 1j * rng.normal(size=samples)
    ) / np.sqrt(2)
    return los + scatter


def main():
    rng = np.random.default_rng(14)
    samples = 80_000
    k_factors = [0, 3, 10]

    plt.figure(figsize=(8, 5))
    for k in k_factors:
        h = rician_fading(k, samples, rng)
        plt.hist(np.abs(h), bins=80, density=True, histtype="step", label=f"K = {k}")

    plt.title("Rician Fading Amplitude Distribution")
    plt.xlabel("Amplitude")
    plt.ylabel("Probability Density")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
