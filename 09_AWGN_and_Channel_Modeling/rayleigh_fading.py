import numpy as np
import matplotlib.pyplot as plt


def main():
    rng = np.random.default_rng(13)
    samples = 50_000
    fading = (rng.normal(size=samples) + 1j * rng.normal(size=samples)) / np.sqrt(2)
    amplitude = np.abs(fading)

    bits = rng.integers(0, 2, samples)
    symbols = 2 * bits - 1
    noise = 0.2 * (rng.normal(size=samples) + 1j * rng.normal(size=samples))
    received = fading * symbols + noise
    equalized = received / fading

    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    axes[0].hist(amplitude, bins=80, density=True)
    axes[0].set_title("Rayleigh Fading Amplitude")
    axes[0].set_xlabel("Amplitude")
    axes[0].grid(True)
    axes[1].scatter(equalized.real[:2000], equalized.imag[:2000], s=6, alpha=0.5)
    axes[1].set_title("Equalized BPSK through Rayleigh Channel")
    axes[1].set_xlabel("I")
    axes[1].set_ylabel("Q")
    axes[1].grid(True)
    axes[1].axis("equal")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
