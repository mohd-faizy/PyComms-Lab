import numpy as np
import matplotlib.pyplot as plt


def main():
    rng = np.random.default_rng(42)
    bits = rng.integers(0, 2, 120)
    symbols = 2 * bits - 1
    channel = np.array([0.9, 0.35, -0.18])
    received = np.convolve(symbols, channel, mode="same") + 0.12 * rng.normal(size=symbols.size)

    equalizer = np.array([0.2, 0.95, -0.28])
    equalized = np.convolve(received, equalizer, mode="same")
    decisions_before = (received >= 0).astype(int)
    decisions_after = (equalized >= 0).astype(int)

    print(f"Errors before equalization: {np.sum(decisions_before != bits)}")
    print(f"Errors after equalization: {np.sum(decisions_after != bits)}")

    plt.figure(figsize=(10, 5))
    plt.plot(symbols[:60], "o-", label="Transmitted")
    plt.plot(received[:60], "s-", label="Received with ISI")
    plt.plot(equalized[:60], "x-", label="Equalized")
    plt.title("Simple Linear Equalization")
    plt.xlabel("Symbol Index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
