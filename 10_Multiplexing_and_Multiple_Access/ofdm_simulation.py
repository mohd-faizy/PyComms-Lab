import numpy as np
import matplotlib.pyplot as plt


def qpsk_symbols(bits):
    pairs = bits.reshape(-1, 2)
    return ((2 * pairs[:, 0] - 1) + 1j * (2 * pairs[:, 1] - 1)) / np.sqrt(2)


def main():
    rng = np.random.default_rng(21)
    n_subcarriers = 64
    cyclic_prefix = 16
    active = np.r_[6:32, 33:59]
    bits = rng.integers(0, 2, active.size * 2)
    symbols = qpsk_symbols(bits)

    frequency_bins = np.zeros(n_subcarriers, dtype=complex)
    frequency_bins[active] = symbols
    time_symbol = np.fft.ifft(frequency_bins)
    tx = np.r_[time_symbol[-cyclic_prefix:], time_symbol]
    rx_bins = np.fft.fft(tx[cyclic_prefix:])

    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    axes[0].plot(np.real(tx), label="Real")
    axes[0].plot(np.imag(tx), label="Imaginary")
    axes[0].set_title("OFDM Time-domain Symbol with Cyclic Prefix")
    axes[0].grid(True)
    axes[0].legend()
    axes[1].scatter(rx_bins[active].real, rx_bins[active].imag)
    axes[1].set_title("Recovered QPSK Subcarriers")
    axes[1].grid(True)
    axes[1].axis("equal")
    axes[1].set_xlabel("I")
    axes[1].set_ylabel("Q")

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
