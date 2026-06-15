"""Linear FM (chirp) pulse compression simulation.

Demonstrates how a chirp waveform achieves fine range resolution through
matched filtering without increasing peak transmit power.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp, correlate


def main():
    fs = 1e6          # 1 MHz sampling rate
    pulse_width = 50e-6   # 50 us chirp duration
    bandwidth = 200e3     # 200 kHz bandwidth
    f0 = 100e3            # start frequency
    f1 = f0 + bandwidth   # end frequency

    t_pulse = np.arange(0, pulse_width, 1 / fs)
    chirp_signal = chirp(t_pulse, f0=f0, f1=f1, t1=pulse_width, method="linear")

    # Uncompressed pulse (same energy, CW burst)
    cw_pulse = np.cos(2 * np.pi * (f0 + bandwidth / 2) * t_pulse)

    # Simulate two targets at different ranges
    c = 3e8
    r1, r2 = 5000, 5100  # metres - 100 m apart
    delay1 = int(2 * r1 / c * fs)
    delay2 = int(2 * r2 / c * fs)

    n_total = delay2 + len(t_pulse) + 500
    received = np.zeros(n_total)
    received[delay1:delay1 + len(chirp_signal)] += chirp_signal
    received[delay2:delay2 + len(chirp_signal)] += 0.7 * chirp_signal

    # Matched filter (time-reversed chirp)
    matched = chirp_signal[::-1]
    compressed = correlate(received, matched, mode="same")
    compressed /= np.max(np.abs(compressed))

    # CW comparison (poor resolution)
    received_cw = np.zeros(n_total)
    received_cw[delay1:delay1 + len(cw_pulse)] += cw_pulse
    received_cw[delay2:delay2 + len(cw_pulse)] += 0.7 * cw_pulse
    cw_corr = correlate(received_cw, cw_pulse[::-1], mode="same")
    cw_corr /= np.max(np.abs(cw_corr))

    t_axis = np.arange(n_total) / fs * 1e6  # microseconds
    range_axis = np.arange(n_total) / fs * c / 2  # metres

    fig, axes = plt.subplots(3, 2, figsize=(14, 10))

    # Chirp waveform
    axes[0, 0].plot(t_pulse * 1e6, chirp_signal, lw=0.5, color="tab:blue")
    axes[0, 0].set_title("Chirp (LFM) Pulse")
    axes[0, 0].set_xlabel("Time (us)")
    axes[0, 0].grid(True)

    # Chirp spectrogram
    axes[0, 1].specgram(chirp_signal, NFFT=64, Fs=fs, noverlap=60,
                        cmap="inferno")
    axes[0, 1].set_title("Chirp Spectrogram")
    axes[0, 1].set_xlabel("Time (s)")
    axes[0, 1].set_ylabel("Frequency (Hz)")

    # Received signal
    axes[1, 0].plot(range_axis, received, lw=0.5, color="tab:orange")
    axes[1, 0].set_title("Received Signal (two targets)")
    axes[1, 0].set_xlabel("Range (m)")
    axes[1, 0].set_xlim(4800, 5400)
    axes[1, 0].grid(True)

    # Compressed output
    axes[1, 1].plot(range_axis, np.abs(compressed), lw=1, color="tab:green")
    axes[1, 1].set_title("After Pulse Compression (matched filter)")
    axes[1, 1].set_xlabel("Range (m)")
    axes[1, 1].set_xlim(4800, 5400)
    axes[1, 1].grid(True)

    # CW comparison
    axes[2, 0].plot(range_axis, np.abs(cw_corr), lw=1, color="tab:red")
    axes[2, 0].set_title("CW Pulse (no compression) - cannot resolve targets")
    axes[2, 0].set_xlabel("Range (m)")
    axes[2, 0].set_xlim(4800, 5400)
    axes[2, 0].grid(True)

    # Resolution comparison
    range_res_chirp = c / (2 * bandwidth)
    range_res_cw = c * pulse_width / 2
    labels = ["Chirp (compressed)", "CW (uncompressed)"]
    res = [range_res_chirp, range_res_cw]
    axes[2, 1].barh(labels, res, color=["tab:green", "tab:red"])
    axes[2, 1].set_title("Range Resolution Comparison")
    axes[2, 1].set_xlabel("Range Resolution (m)")
    for i, v in enumerate(res):
        axes[2, 1].text(v + 10, i, f"{v:.0f} m", va="center")
    axes[2, 1].grid(True, alpha=0.3)

    fig.suptitle("Pulse Compression - Chirp Matched Filtering", fontsize=13)
    fig.tight_layout()
    plt.show()

    print(f"Chirp bandwidth: {bandwidth/1000:.0f} kHz")
    print(f"Pulse width: {pulse_width*1e6:.0f} us")
    print(f"Compression ratio: {pulse_width * bandwidth:.0f}")
    print(f"Range resolution (chirp): {range_res_chirp:.1f} m")
    print(f"Range resolution (CW):    {range_res_cw:.0f} m")


if __name__ == "__main__":
    main()
