import numpy as np
import matplotlib.pyplot as plt


def main():
    fs = 1000
    duration = 1.0
    t = np.arange(0, duration, 1 / fs)
    x = (
        1.0 * np.sin(2 * np.pi * 50 * t)
        + 0.6 * np.sin(2 * np.pi * 120 * t)
        + 0.2 * np.random.default_rng(0).normal(size=t.size)
    )

    freqs = np.fft.rfftfreq(t.size, 1 / fs)
    spectrum = np.abs(np.fft.rfft(x)) / t.size

    fig, axes = plt.subplots(2, 1, figsize=(10, 6))
    axes[0].plot(t[:250], x[:250])
    axes[0].set_title("Signal in Time Domain")
    axes[0].set_xlabel("Time (s)")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(True)

    axes[1].stem(freqs, 2 * spectrum, basefmt=" ")
    axes[1].set_xlim(0, 200)
    axes[1].set_title("Single-sided FFT Magnitude")
    axes[1].set_xlabel("Frequency (Hz)")
    axes[1].set_ylabel("Magnitude")
    axes[1].grid(True)

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
