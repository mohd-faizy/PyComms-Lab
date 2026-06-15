import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc


def main():
    received_power_dbm = np.linspace(-35, -5, 200)
    received_power_w = 1e-3 * 10 ** (received_power_dbm / 10)
    responsivity = 0.8
    noise_std = 0.7e-6
    photocurrent = responsivity * received_power_w
    q_factor = photocurrent / (2 * noise_std)
    ber = 0.5 * erfc(q_factor / np.sqrt(2))

    plt.figure(figsize=(8, 5))
    plt.semilogy(received_power_dbm, ber)
    plt.title("Simplified OOK Optical Link BER")
    plt.xlabel("Received Optical Power (dBm)")
    plt.ylabel("BER")
    plt.grid(True, which="both")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
