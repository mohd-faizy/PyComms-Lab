import numpy as np
import matplotlib.pyplot as plt


def qam16_symbols(bits):
    groups = bits.reshape(-1, 4)
    levels = {
        (0, 0): -3,
        (0, 1): -1,
        (1, 1): 1,
        (1, 0): 3,
    }
    symbols = []
    for group in groups:
        i = levels[tuple(group[:2])]
        q = levels[tuple(group[2:])]
        symbols.append(i + 1j * q)
    return np.array(symbols) / np.sqrt(10)


def main():
    rng = np.random.default_rng(7)
    bits = rng.integers(0, 2, 400)
    symbols = qam16_symbols(bits)
    noise = 0.08 * (rng.normal(size=symbols.size) + 1j * rng.normal(size=symbols.size))
    received = symbols + noise

    plt.figure(figsize=(6, 6))
    plt.scatter(received.real, received.imag, s=18, alpha=0.7, label="Received")
    plt.scatter(symbols.real, symbols.imag, s=40, marker="x", label="Ideal")
    plt.title("16-QAM Constellation with Noise")
    plt.xlabel("In-phase")
    plt.ylabel("Quadrature")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
