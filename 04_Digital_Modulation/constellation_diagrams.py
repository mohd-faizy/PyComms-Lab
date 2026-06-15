import numpy as np
import matplotlib.pyplot as plt


def add_awgn(symbols, snr_db, rng):
    snr_linear = 10 ** (snr_db / 10)
    noise_power = np.mean(np.abs(symbols) ** 2) / snr_linear
    noise = np.sqrt(noise_power / 2) * (
        rng.normal(size=symbols.size) + 1j * rng.normal(size=symbols.size)
    )
    return symbols + noise


def main():
    rng = np.random.default_rng(2)
    bpsk = np.array([-1, 1])
    qpsk = np.array([1 + 1j, -1 + 1j, -1 - 1j, 1 - 1j]) / np.sqrt(2)
    qam16 = np.array([i + 1j * q for i in (-3, -1, 1, 3) for q in (-3, -1, 1, 3)]) / np.sqrt(10)

    constellations = {
        "BPSK": np.repeat(bpsk, 80),
        "QPSK": np.repeat(qpsk, 60),
        "16-QAM": np.repeat(qam16, 25),
    }

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    for ax, (title, symbols) in zip(axes, constellations.items()):
        noisy = add_awgn(symbols, snr_db=15, rng=rng)
        ax.scatter(noisy.real, noisy.imag, s=12, alpha=0.6)
        ax.set_title(title)
        ax.axhline(0, color="black", linewidth=0.8)
        ax.axvline(0, color="black", linewidth=0.8)
        ax.grid(True)
        ax.axis("equal")
        ax.set_xlabel("I")
        ax.set_ylabel("Q")

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
