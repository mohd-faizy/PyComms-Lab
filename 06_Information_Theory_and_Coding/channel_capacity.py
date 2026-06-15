import numpy as np
import matplotlib.pyplot as plt


def main():
    bandwidth = 1e6
    snr_db = np.linspace(-5, 30, 100)
    snr_linear = 10 ** (snr_db / 10)
    capacity = bandwidth * np.log2(1 + snr_linear)

    print(f"Capacity at 10 dB SNR and 1 MHz bandwidth: {bandwidth * np.log2(11) / 1e6:.3f} Mbps")

    plt.figure(figsize=(8, 5))
    plt.plot(snr_db, capacity / 1e6)
    plt.title("Shannon Channel Capacity")
    plt.xlabel("SNR (dB)")
    plt.ylabel("Capacity (Mbps)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
