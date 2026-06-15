import numpy as np
import matplotlib.pyplot as plt


def dbm(watts):
    return 10 * np.log10(watts / 1e-3)


def main():
    pt = 1.0
    gt = 10
    gr = 10
    frequency = 2.4e9
    wavelength = 3e8 / frequency
    distance = np.logspace(0, 4, 200)
    received_power = pt * gt * gr * (wavelength / (4 * np.pi * distance)) ** 2

    plt.figure(figsize=(8, 5))
    plt.semilogx(distance, dbm(received_power))
    plt.title("Friis Transmission Equation")
    plt.xlabel("Distance (m)")
    plt.ylabel("Received Power (dBm)")
    plt.grid(True, which="both")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
