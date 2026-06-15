import numpy as np
import matplotlib.pyplot as plt


def main():
    fs = 20_000
    t = np.arange(0, 0.1, 1 / fs)
    message1 = np.sin(2 * np.pi * 100 * t)
    message2 = np.sin(2 * np.pi * 250 * t)
    fdm = message1 * np.cos(2 * np.pi * 2000 * t) + message2 * np.cos(2 * np.pi * 5000 * t)

    freqs = np.fft.rfftfreq(t.size, 1 / fs)
    spectrum = np.abs(np.fft.rfft(fdm)) / t.size

    fig, axes = plt.subplots(2, 1, figsize=(10, 6))
    axes[0].plot(t[:500], fdm[:500])
    axes[0].set_title("FDM Composite Signal")
    axes[0].set_xlabel("Time (s)")
    axes[0].grid(True)
    axes[1].plot(freqs, spectrum)
    axes[1].set_xlim(0, 7000)
    axes[1].set_title("FDM Spectrum")
    axes[1].set_xlabel("Frequency (Hz)")
    axes[1].grid(True)

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
