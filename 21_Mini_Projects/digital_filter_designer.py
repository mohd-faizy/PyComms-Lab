import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def design_and_plot_filter(order, cutoff, fs, btype='lowpass'):
    # Design Butterworth filter
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = signal.butter(order, normal_cutoff, btype=btype, analog=False)
    
    # Frequency response
    w, h = signal.freqz(b, a, worN=8000)
    freqs = w * fs / (2 * np.pi)
    mag_db = 20 * np.log10(np.maximum(np.abs(h), 1e-10))
    phase = np.unwrap(np.angle(h))
    
    # Pole-Zero calculation
    z, p, k = signal.tf2zpk(b, a)
    
    fig, axes = plt.subplots(3, 1, figsize=(10, 10))
    fig.suptitle(f"Digital {btype.capitalize()} Butterworth Filter (Order {order})", fontweight='bold', fontsize=14)
    
    # Magnitude Response
    axes[0].plot(freqs, mag_db, color="b", linewidth=2)
    axes[0].axvline(cutoff, color="r", linestyle="--", label=f"Cutoff: {cutoff} Hz")
    axes[0].set_title("Magnitude Response")
    axes[0].set_ylabel("Amplitude (dB)")
    axes[0].grid(True, linestyle="--", alpha=0.7)
    axes[0].legend()
    
    # Phase Response
    axes[1].plot(freqs, phase, color="g", linewidth=2)
    axes[1].axvline(cutoff, color="r", linestyle="--")
    axes[1].set_title("Phase Response")
    axes[1].set_ylabel("Phase (radians)")
    axes[1].grid(True, linestyle="--", alpha=0.7)
    axes[1].set_xlabel("Frequency (Hz)")
    
    # Pole-Zero Plot
    unit_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
    axes[2].add_patch(unit_circle)
    axes[2].scatter(np.real(z), np.imag(z), marker='o', facecolors='none', edgecolors='b', s=80, label='Zeros')
    axes[2].scatter(np.real(p), np.imag(p), marker='x', color='r', s=80, label='Poles')
    axes[2].set_title("Pole-Zero Plot")
    axes[2].set_xlabel("Real")
    axes[2].set_ylabel("Imaginary")
    axes[2].axhline(0, color='k', linewidth=0.5)
    axes[2].axvline(0, color='k', linewidth=0.5)
    axes[2].set_xlim(-1.5, 1.5)
    axes[2].set_ylim(-1.5, 1.5)
    axes[2].set_aspect('equal')
    axes[2].grid(True, alpha=0.3)
    axes[2].legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    fs = 44100
    cutoff = 5000
    order = 4
    print(f"Designing {order}th order lowpass filter with {cutoff}Hz cutoff (fs={fs}Hz)")
    design_and_plot_filter(order, cutoff, fs, btype='lowpass')
