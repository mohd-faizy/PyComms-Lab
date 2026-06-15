import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def signal_with_tone(fs, duration, tone_hz, noise_level):
    rng = np.random.default_rng(51)
    t = np.arange(0, duration, 1 / fs)
    x = np.sin(2 * np.pi * tone_hz * t) + noise_level * rng.normal(size=t.size)
    return t, x


def spectrum(x, fs):
    window = np.hanning(x.size)
    freqs = np.fft.rfftfreq(x.size, 1 / fs)
    mag = 20 * np.log10(np.maximum(np.abs(np.fft.rfft(x * window)), 1e-9))
    return freqs, mag


def main():
    fs = 10_000
    duration = 1.0
    t, x = signal_with_tone(fs, duration, 1000, 0.2)
    freqs, mag = spectrum(x, fs)

    fig, axes = plt.subplots(2, 1, figsize=(10, 7))
    plt.subplots_adjust(bottom=0.2)
    time_line, = axes[0].plot(t[:1000], x[:1000])
    spec_line, = axes[1].plot(freqs, mag)
    axes[0].set_title("Time Signal")
    axes[1].set_title("Spectrum")
    axes[1].set_xlabel("Frequency (Hz)")
    axes[1].set_xlim(0, 5000)
    for ax in axes:
        ax.grid(True)

    slider_axis = fig.add_axes([0.15, 0.06, 0.7, 0.03])
    tone_slider = Slider(slider_axis, "Tone Hz", 100, 4500, valinit=1000)

    def update(_):
        _, updated = signal_with_tone(fs, duration, tone_slider.val, 0.2)
        updated_freqs, updated_mag = spectrum(updated, fs)
        time_line.set_ydata(updated[:1000])
        spec_line.set_data(updated_freqs, updated_mag)
        fig.canvas.draw_idle()

    tone_slider.on_changed(update)
    plt.show()


if __name__ == "__main__":
    main()
