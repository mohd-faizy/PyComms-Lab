import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc


def qpsk_mod(bits):
    pairs = bits.reshape(-1, 2)
    i = 2 * pairs[:, 0] - 1
    q = 2 * pairs[:, 1] - 1
    return (i + 1j * q) / np.sqrt(2)


def qpsk_demod(symbols):
    bits = np.empty(symbols.size * 2, dtype=int)
    bits[0::2] = (symbols.real >= 0).astype(int)
    bits[1::2] = (symbols.imag >= 0).astype(int)
    return bits


def main():
    rng = np.random.default_rng(12)
    snr_db = np.arange(0, 11)
    bits = rng.integers(0, 2, 200_000)
    symbols = qpsk_mod(bits)
    simulated_ber = []

    for value in snr_db:
        ebn0 = 10 ** (value / 10)
        noise = np.sqrt(1 / (4 * ebn0)) * (
            rng.normal(size=symbols.size) + 1j * rng.normal(size=symbols.size)
        )
        detected = qpsk_demod(symbols + noise)
        simulated_ber.append(np.mean(detected != bits))

    theoretical_ber = 0.5 * erfc(np.sqrt(10 ** (snr_db / 10)))

    plt.figure(figsize=(8, 5))
    plt.semilogy(snr_db, simulated_ber, "o-", label="Simulated")
    plt.semilogy(snr_db, theoretical_ber, "s--", label="Theoretical")
    plt.title("QPSK BER vs Eb/N0")
    plt.xlabel("Eb/N0 (dB)")
    plt.ylabel("Bit Error Rate")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
