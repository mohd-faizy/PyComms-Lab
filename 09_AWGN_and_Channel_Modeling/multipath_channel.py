"""Multipath Channel Simulation and Frequency Selective Fading.

Models a multipath propagation channel with multiple reflective paths.
Visualises the Channel Impulse Response (Power Delay Profile) and the Channel
Frequency Response, illustrating frequency-selective fading.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    # Simulation parameters
    fs = 100e6  # Sample rate 100 MHz
    t_step = 1.0 / fs
    t = np.arange(0, 1e-6, t_step)  # 1 microsecond window

    # Define channel paths (delays in seconds, gains, phases in radians)
    # Path 0: Line of Sight (direct)
    # Path 1: Reflection from building 1
    # Path 2: Reflection from ground
    # Path 3: Reflection from building 2
    delays = [0.0, 0.15e-6, 0.35e-6, 0.60e-6]  # in seconds
    gains = [1.0, 0.6, 0.45, 0.25]
    phases = [0.0, np.pi/4, -np.pi/3, np.pi/6]

    # --- Compute Channel Impulse Response (CIR) ---
    # represented as a continuous time-domain plot and discrete stems
    cir_t = np.zeros_like(t, dtype=complex)
    for d, g, p in zip(delays, gains, phases):
        idx = int(np.round(d * fs))
        if idx < len(cir_t):
            cir_t[idx] = g * np.exp(1j * p)

    # --- Compute Channel Frequency Response (CFR) ---
    # via Fast Fourier Transform of the impulse response
    fft_size = 1024
    freqs = np.fft.fftfreq(fft_size, t_step) / 1e6  # to MHz
    cfr = np.fft.fft(cir_t, fft_size)
    
    # Keep only positive frequencies for plot
    pos_indices = freqs >= 0
    freqs = freqs[pos_indices]
    cfr = cfr[pos_indices]
    cfr_db = 20 * np.log10(np.abs(cfr) + 1e-6)

    # --- Pass a signal through the channel ---
    # We will use a raised-cosine pulse to show distortion
    # Pulse duration
    t_pulse = np.linspace(-0.25e-6, 0.25e-6, len(t))
    pulse_width = 0.05e-6  # 50 ns
    pulse = np.sinc(t_pulse / pulse_width) * np.blackman(len(t_pulse))

    # Convolve pulse with channel impulse response
    # We use discrete convolution
    received_signal = np.convolve(pulse, cir_t, mode="same")

    # Plot results
    fig, axes = plt.subplots(3, 1, figsize=(11, 9))

    # Plot 1: Power Delay Profile (Impulse Response)
    axes[0].stem(np.array(delays) * 1e9, gains, linefmt="r-", markerfmt="ro", basefmt="k-", label="Multipath Rays")
    # Add a continuous envelope representation
    axes[0].set_title("Channel Impulse Response / Power Delay Profile", fontsize=11, fontweight="bold")
    axes[0].set_xlabel("Delay (nanoseconds)")
    axes[0].set_ylabel("Linear Gain")
    axes[0].grid(True, linestyle="--", alpha=0.5)
    axes[0].set_xlim(-50, 750)
    for i, (d, g) in enumerate(zip(delays, gains)):
        axes[0].text(d * 1e9 + 10, g, f"Path {i}", fontsize=9)

    # Plot 2: Frequency Response (fading profile)
    axes[1].plot(freqs, cfr_db, color="gray", linewidth=2)
    axes[1].set_title("Channel Frequency Response (Frequency-Selective Fading)", fontsize=11, fontweight="bold")
    axes[1].set_xlabel("Frequency (MHz)")
    axes[1].set_ylabel("Magnitude (dB)")
    axes[1].grid(True, which="both", linestyle="--", alpha=0.5)
    # Highlight coherence bandwidth roughly
    # Delay spread ~ 0.6 us -> Coherence bandwidth ~ 1 / delay_spread = 1.6 MHz
    axes[1].axvspan(10, 20, color="gray", alpha=0.15, label="Deep notch fades")
    axes[1].legend()

    # Plot 3: Signal Distortion in Time Domain
    axes[2].plot(t * 1e9, np.abs(pulse), label="Transmitted Pulse", color="gray", linewidth=2)
    axes[2].plot(t * 1e9, np.abs(received_signal), label="Received Distorted Pulse", color="r", linewidth=2)
    axes[2].set_title("Time-Domain Pulse Distortion (Inter-Symbol Interference)", fontsize=11, fontweight="bold")
    axes[2].set_xlabel("Time (nanoseconds)")
    axes[2].set_ylabel("Normalized Amplitude")
    axes[2].grid(True, linestyle="--", alpha=0.5)
    axes[2].legend()

    plt.suptitle("Multipath Propagation Channel Simulation", fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.show()

    # Print channel stats
    delay_spread = np.sqrt(np.sum(np.array(gains)**2 * (np.array(delays) - np.mean(delays))**2) / np.sum(np.array(gains)**2))
    coherence_bw = 1.0 / (delay_spread + 1e-12)
    print("=== Channel Multipath Parameters ===")
    print(f"Rms Delay Spread:          {delay_spread*1e9:.2f} ns")
    print(f"Approx Coherence Bandwidth: {coherence_bw/1e6:.2f} MHz")


if __name__ == "__main__":
    main()
