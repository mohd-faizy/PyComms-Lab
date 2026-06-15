import numpy as np
import matplotlib.pyplot as plt


def main():
    fs = 100_000
    t = np.arange(0, 0.02, 1 / fs)
    rf_frequency = 18_000
    tone_frequency = 1_000
    rf_signal = (1 + 0.5 * np.cos(2 * np.pi * tone_frequency * t)) * np.cos(2 * np.pi * rf_frequency * t)

    local_oscillator = np.exp(-1j * 2 * np.pi * rf_frequency * t)
    iq_baseband = rf_signal * local_oscillator
    window = np.ones(80) / 80
    iq_filtered = np.convolve(iq_baseband, window, mode="same")

    fig, axes = plt.subplots(2, 1, figsize=(10, 6))
    axes[0].plot(t[:600], rf_signal[:600])
    axes[0].set_title("Received RF Signal")
    axes[0].grid(True)
    axes[1].plot(t[:600], iq_filtered.real[:600], label="I")
    axes[1].plot(t[:600], iq_filtered.imag[:600], label="Q")
    axes[1].set_title("Downconverted IQ Baseband")
    axes[1].set_xlabel("Time (s)")
    axes[1].grid(True)
    axes[1].legend()
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
