import numpy as np
import matplotlib.pyplot as plt


def free_space_loss(distance_m, frequency_hz):
    wavelength = 3e8 / frequency_hz
    return 20 * np.log10(4 * np.pi * distance_m / wavelength)


def log_distance_loss(distance_m, reference_loss_db, exponent, reference_distance_m=1.0):
    return reference_loss_db + 10 * exponent * np.log10(distance_m / reference_distance_m)


def main():
    distance = np.linspace(1, 1000, 500)
    frequency = 2.4e9
    fspl = free_space_loss(distance, frequency)
    urban = log_distance_loss(distance, free_space_loss(1, frequency), exponent=3.5)
    indoor = log_distance_loss(distance, free_space_loss(1, frequency), exponent=2.2)

    plt.figure(figsize=(8, 5))
    plt.semilogx(distance, fspl, label="Free space")
    plt.semilogx(distance, urban, label="Urban, n=3.5")
    plt.semilogx(distance, indoor, label="Indoor, n=2.2")
    plt.title("Path Loss Models at 2.4 GHz")
    plt.xlabel("Distance (m)")
    plt.ylabel("Path Loss (dB)")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
