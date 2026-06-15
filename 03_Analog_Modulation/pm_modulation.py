import numpy as np
import matplotlib.pyplot as plt


def main():
    fs = 50_000
    t = np.arange(0, 0.03, 1 / fs)
    fm = 200
    fc = 3000
    phase_deviation = np.pi / 2

    message = np.sin(2 * np.pi * fm * t)
    carrier = np.cos(2 * np.pi * fc * t)
    pm_signal = np.cos(2 * np.pi * fc * t + phase_deviation * message)

    fig, axes = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
    axes[0].plot(t, message)
    axes[0].set_title("Message Signal")
    axes[1].plot(t, carrier)
    axes[1].set_title("Carrier Signal")
    axes[2].plot(t, pm_signal)
    axes[2].set_title("PM Signal")

    for ax in axes:
        ax.grid(True)
    axes[-1].set_xlabel("Time (s)")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
