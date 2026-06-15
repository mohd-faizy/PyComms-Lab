import numpy as np
import matplotlib.pyplot as plt


def raised_cosine_like_pulse(samples_per_symbol):
    t = np.linspace(-1, 1, samples_per_symbol)
    pulse = np.cos(np.pi * t / 2) ** 2
    return pulse / np.sqrt(np.sum(pulse**2))


def main():
    rng = np.random.default_rng(41)
    samples_per_symbol = 24
    bits = rng.integers(0, 2, 20)
    symbols = 2 * bits - 1
    pulse = raised_cosine_like_pulse(samples_per_symbol)
    tx = np.convolve(np.repeat(symbols, samples_per_symbol), pulse, mode="same")
    rx = tx + 0.25 * rng.normal(size=tx.size)
    matched = np.convolve(rx, pulse[::-1], mode="same")
    sample_points = np.arange(samples_per_symbol // 2, matched.size, samples_per_symbol)
    decisions = (matched[sample_points[: bits.size]] >= 0).astype(int)

    print(f"Detected {np.sum(decisions != bits)} errors out of {bits.size} bits")

    plt.figure(figsize=(10, 5))
    plt.plot(rx, label="Received")
    plt.plot(matched, label="Matched filter output")
    plt.scatter(sample_points[: bits.size], matched[sample_points[: bits.size]], c="red", zorder=3, label="Samples")
    plt.title("Matched Filtering for Binary Pulses")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
