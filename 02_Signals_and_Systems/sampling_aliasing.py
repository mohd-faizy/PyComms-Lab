import numpy as np
import matplotlib.pyplot as plt


def sample_signal(freq_hz, fs, duration):
    t = np.arange(0, duration, 1 / fs)
    return t, np.sin(2 * np.pi * freq_hz * t)


def main():
    signal_freq = 40
    duration = 0.15
    t_cont = np.linspace(0, duration, 3000)
    x_cont = np.sin(2 * np.pi * signal_freq * t_cont)

    sample_rates = [200, 60]
    fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

    for ax, fs in zip(axes, sample_rates):
        t_s, x_s = sample_signal(signal_freq, fs, duration)
        ax.plot(t_cont, x_cont, label="Original 40 Hz signal")
        ax.stem(t_s, x_s, linefmt="C1-", markerfmt="C1o", basefmt=" ", label=f"Samples at {fs} Hz")
        ax.set_title(f"Sampling at {fs} Hz")
        ax.grid(True)
        ax.legend()

    axes[-1].set_xlabel("Time (s)")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
