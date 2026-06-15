import numpy as np
import matplotlib.pyplot as plt


def main():
    distance_km = np.linspace(0, 100, 300)
    input_power_mw = 1.0
    attenuation_db_per_km = 0.2
    output_power_mw = input_power_mw * 10 ** (-attenuation_db_per_km * distance_km / 10)

    print(f"Power after 50 km: {np.interp(50, distance_km, output_power_mw):.4f} mW")

    plt.figure(figsize=(8, 5))
    plt.plot(distance_km, output_power_mw)
    plt.title("Optical Fiber Attenuation")
    plt.xlabel("Fiber Length (km)")
    plt.ylabel("Output Power (mW)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
