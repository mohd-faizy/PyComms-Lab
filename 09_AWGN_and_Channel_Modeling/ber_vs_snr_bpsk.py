import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc


def main():
    rng = np.random.default_rng(11)
    snr_db = np.arange(0, 11)
    bits = rng.integers(0, 2, 200_000)
    symbols = 2 * bits - 1
    simulated_ber = []

    for value in snr_db:
        ebn0 = 10 ** (value / 10)
        noise = rng.normal(scale=np.sqrt(1 / (2 * ebn0)), size=symbols.size)
        received = symbols + noise
        detected = (received >= 0).astype(int)
        simulated_ber.append(np.mean(detected != bits))

    theoretical_ber = 0.5 * erfc(np.sqrt(10 ** (snr_db / 10)))

    plt.figure(figsize=(8, 5))
    plt.semilogy(snr_db, simulated_ber, "o-", label="Simulated")
    plt.semilogy(snr_db, theoretical_ber, "s--", label="Theoretical")
    plt.title("BPSK BER vs Eb/N0")
    plt.xlabel("Eb/N0 (dB)")
    plt.ylabel("Bit Error Rate")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
