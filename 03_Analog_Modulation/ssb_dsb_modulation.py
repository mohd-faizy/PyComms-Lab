import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert


def spectrum(signal_values, fs):
    freqs = np.fft.fftshift(np.fft.fftfreq(signal_values.size, 1 / fs))
    mag = np.abs(np.fft.fftshift(np.fft.fft(signal_values))) / signal_values.size
    return freqs, mag


def main():
    fs = 20_000
    t = np.arange(0, 0.04, 1 / fs)
    fm = 300
    fc = 3000

    message = np.cos(2 * np.pi * fm * t)
    dsb_sc = message * np.cos(2 * np.pi * fc * t)
    analytic_message = hilbert(message)
    ssb_usb = np.real(analytic_message * np.exp(1j * 2 * np.pi * fc * t))

    freqs_dsb, mag_dsb = spectrum(dsb_sc, fs)
    freqs_ssb, mag_ssb = spectrum(ssb_usb, fs)

    fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    axes[0].plot(freqs_dsb, mag_dsb)
    axes[0].set_title("DSB-SC Spectrum")
    axes[1].plot(freqs_ssb, mag_ssb)
    axes[1].set_title("SSB USB Spectrum")

    for ax in axes:
        ax.set_xlim(-5000, 5000)
        ax.grid(True)
        ax.set_ylabel("Magnitude")
    axes[-1].set_xlabel("Frequency (Hz)")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
