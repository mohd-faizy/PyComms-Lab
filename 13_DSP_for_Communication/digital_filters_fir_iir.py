import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, firwin, freqz, lfilter


def main():
    fs = 2000
    cutoff = 200
    t = np.arange(0, 1, 1 / fs)
    signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 500 * t)

    fir_coeff = firwin(numtaps=51, cutoff=cutoff, fs=fs)
    b_iir, a_iir = butter(5, cutoff, fs=fs)
    fir_output = lfilter(fir_coeff, 1, signal)
    iir_output = lfilter(b_iir, a_iir, signal)

    w_fir, h_fir = freqz(fir_coeff, worN=1024, fs=fs)
    w_iir, h_iir = freqz(b_iir, a_iir, worN=1024, fs=fs)

    fig, axes = plt.subplots(2, 1, figsize=(10, 6))
    axes[0].plot(t[:300], signal[:300], label="Input")
    axes[0].plot(t[:300], fir_output[:300], label="FIR")
    axes[0].plot(t[:300], iir_output[:300], label="IIR")
    axes[0].set_title("Low-pass Filtering")
    axes[0].grid(True)
    axes[0].legend()
    axes[1].plot(w_fir, 20 * np.log10(np.maximum(np.abs(h_fir), 1e-6)), label="FIR")
    axes[1].plot(w_iir, 20 * np.log10(np.maximum(np.abs(h_iir), 1e-6)), label="IIR")
    axes[1].set_title("Magnitude Responses")
    axes[1].set_xlabel("Frequency (Hz)")
    axes[1].set_ylabel("Magnitude (dB)")
    axes[1].grid(True)
    axes[1].legend()

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
