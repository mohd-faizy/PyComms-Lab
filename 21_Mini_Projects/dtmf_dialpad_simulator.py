import numpy as np
import matplotlib.pyplot as plt

# DTMF Frequencies
ROW_FREQS = [697, 770, 852, 941]
COL_FREQS = [1209, 1336, 1477, 1633]

KEYPAD = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2), 'A': (0, 3),
    '4': (1, 0), '5': (1, 1), '6': (1, 2), 'B': (1, 3),
    '7': (2, 0), '8': (2, 1), '9': (2, 2), 'C': (2, 3),
    '*': (3, 0), '0': (3, 1), '#': (3, 2), 'D': (3, 3)
}

def generate_dtmf(key, fs=8000, duration=0.2):
    key = key.upper()
    if key not in KEYPAD:
        raise ValueError(f"Invalid key: {key}")
    
    r, c = KEYPAD[key]
    f1, f2 = ROW_FREQS[r], COL_FREQS[c]
    
    t = np.arange(0, duration, 1/fs)
    signal = 0.5 * np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)
    return t, signal, f1, f2

def plot_dtmf(key="5"):
    fs = 8000
    t, signal, f1, f2 = generate_dtmf(key, fs)
    
    # Spectrum
    N = len(signal)
    freqs = np.fft.rfftfreq(N, 1/fs)
    mag = np.abs(np.fft.rfft(signal)) / N
    
    fig, axes = plt.subplots(2, 1, figsize=(10, 6))
    
    # Time domain (zoomed in to see the wave)
    samples_to_plot = int(0.02 * fs) # 20 ms
    axes[0].plot(t[:samples_to_plot] * 1000, signal[:samples_to_plot], color="b", linewidth=1.5)
    axes[0].set_title(f"DTMF Signal for Key '{key}' (Time Domain)")
    axes[0].set_xlabel("Time (ms)")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(True, linestyle="--", alpha=0.7)
    
    # Frequency domain
    axes[1].plot(freqs, mag, color="r", linewidth=2)
    axes[1].axvline(f1, color="k", linestyle="--", alpha=0.5, label=f"Row Freq: {f1} Hz")
    axes[1].axvline(f2, color="gray", linestyle="--", alpha=0.5, label=f"Col Freq: {f2} Hz")
    axes[1].set_title("DTMF Spectrum")
    axes[1].set_xlabel("Frequency (Hz)")
    axes[1].set_ylabel("Magnitude")
    axes[1].set_xlim(500, 2000)
    axes[1].grid(True, linestyle="--", alpha=0.7)
    axes[1].legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Generating DTMF for key '5'...")
    plot_dtmf("5")
