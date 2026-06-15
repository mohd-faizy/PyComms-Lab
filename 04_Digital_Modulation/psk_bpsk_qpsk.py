import numpy as np
import matplotlib.pyplot as plt


def bpsk_symbols(bits):
    return 2 * bits - 1


def qpsk_symbols(bits):
    pairs = bits.reshape(-1, 2)
    mapping = {
        (0, 0): 1 + 1j,
        (0, 1): -1 + 1j,
        (1, 1): -1 - 1j,
        (1, 0): 1 - 1j,
    }
    return np.array([mapping[tuple(pair)] for pair in pairs]) / np.sqrt(2)


def main():
    rng = np.random.default_rng(4)
    bits = rng.integers(0, 2, 64)
    bpsk = bpsk_symbols(bits)
    qpsk = qpsk_symbols(bits[:64])

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].scatter(bpsk.real, np.zeros_like(bpsk), c=bits)
    axes[0].set_title("BPSK Constellation")
    axes[1].scatter(qpsk.real, qpsk.imag)
    axes[1].set_title("QPSK Constellation")

    for ax in axes:
        ax.axhline(0, color="black", linewidth=0.8)
        ax.axvline(0, color="black", linewidth=0.8)
        ax.set_xlabel("In-phase")
        ax.set_ylabel("Quadrature")
        ax.grid(True)
        ax.axis("equal")

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
