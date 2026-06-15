import numpy as np
import matplotlib.pyplot as plt


def main():
    distance_km = np.linspace(1, 100, 400)
    frequency_mhz = 1.0
    surface_factors = {
        "Sea water": 0.015,
        "Wet ground": 0.04,
        "Dry ground": 0.08,
    }

    plt.figure(figsize=(8, 5))
    for label, attenuation_factor in surface_factors.items():
        loss_db = 20 * np.log10(distance_km) + attenuation_factor * frequency_mhz * distance_km
        plt.plot(distance_km, loss_db, label=label)

    plt.title("Simplified Ground-wave Propagation Loss")
    plt.xlabel("Distance (km)")
    plt.ylabel("Relative Loss (dB)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
