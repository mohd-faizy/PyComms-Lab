"""Random processes: autocorrelation and power spectral density.

Simulates a wide-sense stationary (WSS) random process, computes its
autocorrelation function, and derives the power spectral density via the
Wiener-Khinchin theorem.
"""

import numpy as np
import matplotlib.pyplot as plt


def autocorrelation(x, max_lag=None):
    """Estimate the autocorrelation of a zero-mean signal."""
    n = len(x)
    if max_lag is None:
        max_lag = n // 2
    x = x - np.mean(x)
    result = np.correlate(x, x, mode="full")
    result = result[n - 1:]  # positive lags only
    return result[:max_lag] / result[0]


def main():
    rng = np.random.default_rng(42)
    fs = 1000
    n_samples = 4096
    t = np.arange(n_samples) / fs

    # Generate a band-limited random process (filtered white noise)
    white_noise = rng.standard_normal(n_samples)
    # Simple low-pass via moving average (creates a coloured process)
    kernel_len = 30
    kernel = np.ones(kernel_len) / kernel_len
    coloured = np.convolve(white_noise, kernel, mode="same")

    # --- Autocorrelation ---
    max_lag = 200
    lags = np.arange(max_lag) / fs
    r_white = autocorrelation(white_noise, max_lag)
    r_coloured = autocorrelation(coloured, max_lag)

    # --- PSD via Welch-like FFT (Wiener-Khinchin) ---
    freqs_w = np.fft.rfftfreq(n_samples, 1 / fs)
    psd_white = np.abs(np.fft.rfft(white_noise)) ** 2 / n_samples
    psd_coloured = np.abs(np.fft.rfft(coloured)) ** 2 / n_samples

    fig, axes = plt.subplots(2, 2, figsize=(13, 8))

    axes[0, 0].plot(t[:500], white_noise[:500], alpha=0.8)
    axes[0, 0].set_title("White Noise (WSS)")
    axes[0, 0].set_xlabel("Time (s)")
    axes[0, 0].grid(True)

    axes[0, 1].plot(t[:500], coloured[:500], alpha=0.8, color="tab:orange")
    axes[0, 1].set_title("Coloured Noise (filtered)")
    axes[0, 1].set_xlabel("Time (s)")
    axes[0, 1].grid(True)

    axes[1, 0].plot(lags, r_white, label="White")
    axes[1, 0].plot(lags, r_coloured, label="Coloured")
    axes[1, 0].set_title("Autocorrelation R(tau)")
    axes[1, 0].set_xlabel("Lag tau (s)")
    axes[1, 0].legend()
    axes[1, 0].grid(True)

    axes[1, 1].semilogy(freqs_w, psd_white, alpha=0.6, label="White")
    axes[1, 1].semilogy(freqs_w, psd_coloured, alpha=0.8, label="Coloured")
    axes[1, 1].set_title("Power Spectral Density S(f)")
    axes[1, 1].set_xlabel("Frequency (Hz)")
    axes[1, 1].legend()
    axes[1, 1].grid(True)

    fig.suptitle("Random Processes - Autocorrelation & PSD", fontsize=13)
    fig.tight_layout()
    plt.show()

    print(f"White noise mean: {white_noise.mean():.4f}, var: {white_noise.var():.4f}")
    print(f"Coloured noise mean: {coloured.mean():.4f}, var: {coloured.var():.4f}")


if __name__ == "__main__":
    main()
