import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfiltfilt


def lowpass(x, cutoff_hz, fs, order=5):
    sos = butter(order, cutoff_hz, fs=fs, output="sos")
    return sosfiltfilt(sos, x)


def main():
    fs = 200_000
    t = np.arange(0, 0.005, 1 / fs)
    rf = 40_000
    if_freq = 10_000
    lo = rf - if_freq
    message_freq = 1000

    message = 0.6 * np.cos(2 * np.pi * message_freq * t)
    rf_signal = (1 + message) * np.cos(2 * np.pi * rf * t)
    mixer_output = rf_signal * np.cos(2 * np.pi * lo * t)
    if_signal = lowpass(mixer_output, 20_000, fs)

    fig, axes = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
    axes[0].plot(t * 1000, rf_signal)
    axes[0].set_title("Received RF Signal")
    axes[1].plot(t * 1000, mixer_output)
    axes[1].set_title("Mixer Output")
    axes[2].plot(t * 1000, if_signal)
    axes[2].set_title(f"Filtered IF Signal near {if_freq / 1000:.0f} kHz")

    for ax in axes:
        ax.grid(True)
    axes[-1].set_xlabel("Time (ms)")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
