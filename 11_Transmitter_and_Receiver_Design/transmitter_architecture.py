"""Transmitter architecture simulation.

Simulates a complete transmitter chain:
  Message source -> Source encoding -> Modulator -> Up-converter -> Power amp
Includes power amplifier non-linearity modelling.
"""

import numpy as np
import matplotlib.pyplot as plt


def pa_model(signal, gain=10.0, saturation=8.0):
    """Simplified Rapp power amplifier model with saturation."""
    linear = gain * signal
    return saturation * np.tanh(linear / saturation)


def main():
    fs = 200_000
    t = np.arange(0, 0.01, 1 / fs)
    fc = 20_000  # carrier frequency
    fm = 1000    # message frequency

    # --- Stage 1: Message Source ---
    message = np.sin(2 * np.pi * fm * t)

    # --- Stage 2: Modulation (DSBSC-AM) ---
    modulated = message * np.cos(2 * np.pi * fc * t)

    # --- Stage 3: Up-conversion (frequency translation) ---
    f_lo = 30_000
    upconverted = modulated * np.cos(2 * np.pi * f_lo * t)

    # --- Stage 4: Power Amplifier ---
    pa_linear = pa_model(upconverted, gain=2.0, saturation=50)
    pa_saturated = pa_model(upconverted, gain=5.0, saturation=3.0)

    fig, axes = plt.subplots(3, 2, figsize=(14, 10))

    # Message
    axes[0, 0].plot(t * 1000, message, color="tab:blue")
    axes[0, 0].set_title("1. Message Source")
    axes[0, 0].grid(True)

    # Modulated
    axes[0, 1].plot(t * 1000, modulated, lw=0.5, color="tab:orange")
    axes[0, 1].set_title("2. Modulated (DSBSC-AM)")
    axes[0, 1].grid(True)

    # Up-converted
    axes[1, 0].plot(t * 1000, upconverted, lw=0.3, color="tab:green")
    axes[1, 0].set_title("3. Up-converted (RF)")
    axes[1, 0].grid(True)

    # PA comparison
    axes[1, 1].plot(t * 1000, pa_linear, lw=0.4, label="Linear PA", alpha=0.8)
    axes[1, 1].plot(t * 1000, pa_saturated, lw=0.4, label="Saturated PA", alpha=0.8)
    axes[1, 1].set_title("4. Power Amplifier Output")
    axes[1, 1].legend()
    axes[1, 1].grid(True)

    # PA characteristic curve
    x = np.linspace(-5, 5, 500)
    axes[2, 0].plot(x, pa_model(x, gain=2, saturation=50), label="Linear region")
    axes[2, 0].plot(x, pa_model(x, gain=5, saturation=3), label="Saturated")
    axes[2, 0].set_title("PA Transfer Characteristic")
    axes[2, 0].set_xlabel("Input Amplitude")
    axes[2, 0].set_ylabel("Output Amplitude")
    axes[2, 0].legend()
    axes[2, 0].grid(True)

    # Spectrum comparison
    freqs = np.fft.rfftfreq(len(t), 1 / fs)
    spec_lin = np.abs(np.fft.rfft(pa_linear)) / len(t)
    spec_sat = np.abs(np.fft.rfft(pa_saturated)) / len(t)
    axes[2, 1].semilogy(freqs / 1000, spec_lin, alpha=0.7, label="Linear PA")
    axes[2, 1].semilogy(freqs / 1000, spec_sat, alpha=0.7, label="Saturated PA")
    axes[2, 1].set_title("Output Spectrum (harmonics from saturation)")
    axes[2, 1].set_xlabel("Frequency (kHz)")
    axes[2, 1].set_xlim(0, 80)
    axes[2, 1].legend()
    axes[2, 1].grid(True, which="both")

    fig.suptitle("Complete Transmitter Architecture", fontsize=13)
    fig.tight_layout()
    plt.show()

    print("Transmitter chain: Source -> Modulator -> Up-converter -> PA")
    print("PA saturation introduces spectral regrowth (unwanted harmonics).")


if __name__ == "__main__":
    main()
