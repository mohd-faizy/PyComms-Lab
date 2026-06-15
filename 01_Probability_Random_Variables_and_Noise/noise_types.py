"""Noise types in communication systems.

Simulates and compares thermal (Johnson-Nyquist) noise, shot noise, and
flicker (1/f) noise.  Each is plotted in time domain and its PSD is shown
to highlight the spectral differences.
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_thermal_noise(n, power, rng):
    """Gaussian white noise modelling thermal noise."""
    return rng.normal(scale=np.sqrt(power), size=n)


def generate_shot_noise(n, rate, rng):
    """Poisson-process based shot noise."""
    return rng.poisson(lam=rate, size=n).astype(float) - rate


def generate_flicker_noise(n, rng):
    """1/f noise generated via spectral shaping of white noise."""
    white = rng.standard_normal(n)
    spectrum = np.fft.rfft(white)
    freqs = np.fft.rfftfreq(n)
    freqs[0] = 1  # avoid divide-by-zero
    spectrum /= np.sqrt(freqs)
    return np.fft.irfft(spectrum, n=n)


def main():
    rng = np.random.default_rng(7)
    n = 4096
    fs = 10000
    t = np.arange(n) / fs

    thermal = generate_thermal_noise(n, power=0.5, rng=rng)
    shot = generate_shot_noise(n, rate=10, rng=rng)
    flicker = generate_flicker_noise(n, rng=rng)

    # Normalise for visual comparison
    shot = shot / np.std(shot) * np.std(thermal)
    flicker = flicker / np.std(flicker) * np.std(thermal)

    noises = [
        ("Thermal Noise (White / Gaussian)", thermal, "tab:blue"),
        ("Shot Noise (Poisson)", shot, "tab:orange"),
        ("Flicker Noise (1/f)", flicker, "tab:green"),
    ]

    fig, axes = plt.subplots(3, 2, figsize=(14, 9))
    freqs = np.fft.rfftfreq(n, 1 / fs)

    for i, (name, sig, colour) in enumerate(noises):
        axes[i, 0].plot(t[:600], sig[:600], alpha=0.8, color=colour)
        axes[i, 0].set_title(f"{name} - Time Domain")
        axes[i, 0].set_xlabel("Time (s)")
        axes[i, 0].grid(True)

        psd = np.abs(np.fft.rfft(sig)) ** 2 / n
        axes[i, 1].semilogy(freqs, psd, alpha=0.8, color=colour)
        axes[i, 1].set_title(f"{name} - PSD")
        axes[i, 1].set_xlabel("Frequency (Hz)")
        axes[i, 1].grid(True)

    fig.suptitle("Noise Types in Communication Systems", fontsize=13)
    fig.tight_layout()
    plt.show()

    for name, sig, _ in noises:
        print(f"{name:45s} | mean={sig.mean():+.4f}, std={sig.std():.4f}")


if __name__ == "__main__":
    main()
