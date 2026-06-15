import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def square_wave_series(t, fundamental_hz, harmonics):
    result = np.zeros_like(t)
    for n in range(1, harmonics + 1, 2):
        result += np.sin(2 * np.pi * n * fundamental_hz * t) / n
    return (4 / np.pi) * result


def main():
    f0 = 2
    t = np.linspace(0, 2, 2000, endpoint=False)
    ideal = signal.square(2 * np.pi * f0 * t)

    plt.figure(figsize=(10, 5))
    plt.plot(t, ideal, "k--", linewidth=1, label="Ideal square wave")
    for harmonics in (1, 3, 9, 25):
        plt.plot(t, square_wave_series(t, f0, harmonics), label=f"{harmonics} harmonics")

    plt.title("Fourier Series Approximation of a Square Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
