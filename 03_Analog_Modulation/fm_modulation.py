import numpy as np
import matplotlib.pyplot as plt


def main():
    fs = 50_000
    t = np.arange(0, 0.03, 1 / fs)
    fm = 200
    fc = 3000
    freq_deviation = 800

    message = np.sin(2 * np.pi * fm * t)
    phase = 2 * np.pi * fc * t + 2 * np.pi * freq_deviation * np.cumsum(message) / fs
    fm_signal = np.cos(phase)
    instantaneous_frequency = fc + freq_deviation * message

    fig, axes = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
    axes[0].plot(t, message)
    axes[0].set_title("Message Signal")
    axes[1].plot(t, instantaneous_frequency)
    axes[1].set_title("Instantaneous Frequency")
    axes[2].plot(t, fm_signal)
    axes[2].set_title("FM Signal")

    for ax in axes:
        ax.grid(True)
    axes[-1].set_xlabel("Time (s)")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
