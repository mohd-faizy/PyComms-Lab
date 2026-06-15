import numpy as np
import matplotlib.pyplot as plt


def main():
    carrier_frequency = 2.2e9
    speed_of_light = 3e8
    max_radial_velocity = 7_500
    time = np.linspace(-300, 300, 600)
    radial_velocity = max_radial_velocity * np.sin(np.pi * time / time.max())
    doppler_shift = carrier_frequency * radial_velocity / speed_of_light

    print(f"Maximum Doppler shift: {np.max(np.abs(doppler_shift)) / 1000:.2f} kHz")

    plt.figure(figsize=(8, 5))
    plt.plot(time, doppler_shift / 1000)
    plt.title("Satellite Doppler Shift during Pass")
    plt.xlabel("Time from closest approach (s)")
    plt.ylabel("Doppler Shift (kHz)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
