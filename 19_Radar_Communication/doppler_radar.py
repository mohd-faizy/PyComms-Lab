"""Doppler radar simulation for moving-target velocity estimation.

Simulates radar returns from moving targets, extracts Doppler frequency
shifts, and estimates target velocities.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    c = 3e8               # speed of light
    fc = 10e9             # 10 GHz carrier (X-band)
    wavelength = c / fc
    prf = 10_000          # pulse repetition frequency (Hz)
    n_pulses = 256        # number of pulses for Doppler processing
    fs = prf              # slow-time sampling rate = PRF

    # Target velocities (m/s)
    targets = [
        {"v": 30, "range_bin": 50, "rcs": 1.0, "label": "Car (30 m/s)"},
        {"v": 250, "range_bin": 80, "rcs": 0.5, "label": "Aircraft (250 m/s)"},
        {"v": -15, "range_bin": 50, "rcs": 0.3, "label": "Approaching (-15 m/s)"},
    ]

    # Slow-time axis (pulse index)
    slow_time = np.arange(n_pulses) / prf

    # Build slow-time signal for a single range bin
    # Each target contributes a complex exponential at its Doppler frequency
    range_bins = sorted(set(t["range_bin"] for t in targets))

    fig, axes = plt.subplots(2, 2, figsize=(14, 9))

    # Doppler signals per range bin
    for rb in range_bins:
        signal = np.zeros(n_pulses, dtype=complex)
        for t in targets:
            if t["range_bin"] == rb:
                fd = 2 * t["v"] / wavelength  # Doppler frequency
                signal += t["rcs"] * np.exp(1j * 2 * np.pi * fd * slow_time)

        # Add noise
        rng = np.random.default_rng(42)
        noise = 0.1 * (rng.standard_normal(n_pulses) +
                       1j * rng.standard_normal(n_pulses))
        signal += noise

        # Doppler FFT
        doppler_spectrum = np.fft.fftshift(np.fft.fft(signal))
        doppler_freqs = np.fft.fftshift(np.fft.fftfreq(n_pulses, 1 / prf))
        velocities = doppler_freqs * wavelength / 2  # convert to velocity

        axes[0, 0].plot(slow_time * 1000, np.real(signal), lw=0.8,
                       label=f"Range bin {rb}")

    axes[0, 0].set_title("Slow-Time Signal (real part)")
    axes[0, 0].set_xlabel("Time (ms)")
    axes[0, 0].legend()
    axes[0, 0].grid(True)

    # Full Doppler spectrum
    all_signal = np.zeros(n_pulses, dtype=complex)
    for t in targets:
        fd = 2 * t["v"] / wavelength
        all_signal += t["rcs"] * np.exp(1j * 2 * np.pi * fd * slow_time)
    all_signal += noise

    doppler_spectrum = np.fft.fftshift(np.fft.fft(all_signal))
    doppler_freqs = np.fft.fftshift(np.fft.fftfreq(n_pulses, 1 / prf))
    velocities = doppler_freqs * wavelength / 2

    axes[0, 1].plot(velocities, 20 * np.log10(np.abs(doppler_spectrum) + 1e-10),
                   color="tab:blue")
    for t in targets:
        axes[0, 1].axvline(t["v"], ls="--", lw=1, alpha=0.7,
                          label=t["label"])
    axes[0, 1].set_title("Doppler Spectrum")
    axes[0, 1].set_xlabel("Velocity (m/s)")
    axes[0, 1].set_ylabel("Magnitude (dB)")
    axes[0, 1].legend(fontsize=8)
    axes[0, 1].grid(True)

    # Doppler frequency vs velocity
    v_range = np.linspace(-500, 500, 500)
    for f in [3e9, 10e9, 24e9, 77e9]:
        fd = 2 * v_range / (c / f)
        axes[1, 0].plot(v_range, fd / 1000,
                       label=f"{f/1e9:.0f} GHz")
    axes[1, 0].set_title("Doppler Frequency vs Target Velocity")
    axes[1, 0].set_xlabel("Velocity (m/s)")
    axes[1, 0].set_ylabel("Doppler Frequency (kHz)")
    axes[1, 0].legend()
    axes[1, 0].grid(True)

    # Max unambiguous velocity vs PRF
    prf_range = np.logspace(2, 5, 200)
    v_max = prf_range * wavelength / 4
    axes[1, 1].semilogx(prf_range / 1000, v_max, color="tab:red", lw=2)
    axes[1, 1].set_title(f"Max Unambiguous Velocity (fc = {fc/1e9:.0f} GHz)")
    axes[1, 1].set_xlabel("PRF (kHz)")
    axes[1, 1].set_ylabel("V_max (m/s)")
    axes[1, 1].grid(True, which="both")

    fig.suptitle("Doppler Radar - Velocity Estimation", fontsize=13)
    fig.tight_layout()
    plt.show()

    print("=== Detected Targets ===")
    for t in targets:
        fd = 2 * t["v"] / wavelength
        print(f"  {t['label']:25s} | v = {t['v']:+6.0f} m/s | "
              f"fd = {fd:+.1f} Hz")


if __name__ == "__main__":
    main()
