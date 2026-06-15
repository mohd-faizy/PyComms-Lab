"""Frequency-Hopping Spread Spectrum (FHSS) simulation.

Demonstrates frequency hopping driven by a PN sequence.  Generates a
spectrogram showing the hopping pattern across time and frequency.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    rng = np.random.default_rng(55)
    fs = 100_000           # sampling rate
    hop_duration = 0.002   # 2 ms per hop
    n_hops = 40
    n_freqs = 8            # number of frequency slots
    freq_base = 5_000      # lowest carrier frequency
    freq_spacing = 3_000   # spacing between carriers

    hop_samples = int(hop_duration * fs)
    total_samples = hop_samples * n_hops

    # PN-driven hopping sequence
    hop_pattern = rng.integers(0, n_freqs, n_hops)

    # Generate hopped signal
    signal = np.empty(total_samples)
    t_hop = np.arange(hop_samples) / fs
    data_bits = 2 * rng.integers(0, 2, n_hops) - 1  # +/-1 BPSK per hop

    for i in range(n_hops):
        fc = freq_base + hop_pattern[i] * freq_spacing
        segment = data_bits[i] * np.cos(2 * np.pi * fc * t_hop)
        signal[i * hop_samples:(i + 1) * hop_samples] = segment

    t_full = np.arange(total_samples) / fs

    fig, axes = plt.subplots(3, 1, figsize=(14, 10))

    # Time-domain signal
    axes[0].plot(t_full * 1000, signal, lw=0.3, color="tab:blue")
    axes[0].set_title("FHSS Signal - Time Domain")
    axes[0].set_xlabel("Time (ms)")
    axes[0].grid(True)

    # Spectrogram
    axes[1].specgram(signal, NFFT=256, Fs=fs, noverlap=200,
                     cmap="inferno")
    axes[1].set_title("Spectrogram - Frequency Hopping Pattern")
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Frequency (Hz)")

    # Hopping pattern
    hop_times = np.arange(n_hops) * hop_duration * 1000
    hop_freqs = [freq_base + hp * freq_spacing for hp in hop_pattern]
    axes[2].step(hop_times, np.array(hop_freqs) / 1000, where="post",
                color="tab:red", lw=2)
    axes[2].set_title("Hopping Pattern (PN-driven)")
    axes[2].set_xlabel("Time (ms)")
    axes[2].set_ylabel("Carrier Frequency (kHz)")
    axes[2].set_yticks([freq_base / 1000 + i * freq_spacing / 1000
                        for i in range(n_freqs)])
    axes[2].grid(True)

    fig.suptitle(f"FHSS - {n_freqs} frequency slots, {n_hops} hops", fontsize=13)
    fig.tight_layout()
    plt.show()

    print(f"Number of frequency slots: {n_freqs}")
    print(f"Hop duration: {hop_duration * 1000:.0f} ms")
    print(f"Bandwidth: {freq_base} - {freq_base + (n_freqs-1)*freq_spacing} Hz")
    print(f"Hopping pattern (first 10): {hop_pattern[:10].tolist()}")


if __name__ == "__main__":
    main()
