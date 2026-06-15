"""Cognitive Radio Spectrum Sensing Simulation.

Simulates spectrum sensing using energy detection, demonstrating the trade-off
between Probability of Detection (Pd) and Probability of False Alarm (Pfa)
via ROC curves and showing energy distributions under H0 and H1 hypotheses.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2


def simulate_energy_detection(n_samples, snr_db, h_hypothesis, num_trials=2000):
    """Simulate the energy detector over multiple trials.

    h_hypothesis: 0 for H0 (noise only), 1 for H1 (signal + noise)
    """
    snr_linear = 10 ** (snr_db / 10.0)
    # Noise variance is normalized to 1
    noise_std = 1.0

    energies = np.zeros(num_trials)
    for i in range(num_trials):
        noise = np.random.normal(0, noise_std, n_samples)
        if h_hypothesis == 1:
            # Signal is modeled as complex/real Gaussian or deterministic
            # Here we assume a simple real Gaussian signal
            signal = np.random.normal(0, np.sqrt(snr_linear), n_samples)
            received = signal + noise
        else:
            received = noise

        # Energy metric: average or sum of squares of samples
        energies[i] = np.sum(received ** 2)

    return energies


def main():
    n_samples = 50  # Time-bandwidth product (number of samples)
    snr_db = -5     # Low SNR for spectrum sensing demonstration
    num_trials = 5000

    print("=== Cognitive Radio Energy Detection Simulator ===")
    print(f"Number of samples (N): {n_samples}")
    print(f"SNR: {snr_db} dB")

    # Simulate H0 (Noise only) and H1 (Signal + Noise)
    np.random.seed(42)
    energies_h0 = simulate_energy_detection(n_samples, snr_db, 0, num_trials)
    energies_h1 = simulate_energy_detection(n_samples, snr_db, 1, num_trials)

    # Calculate ROC Curve
    # Pd is the fraction of H1 trials exceeding threshold
    # Pfa is the fraction of H0 trials exceeding threshold
    thresholds = np.linspace(np.min(energies_h0), np.max(energies_h1), 200)
    p_fa = []
    p_d = []

    for thresh in thresholds:
        fa = np.sum(energies_h0 > thresh) / num_trials
        d = np.sum(energies_h1 > thresh) / num_trials
        p_fa.append(fa)
        p_d.append(d)

    # Theoretical ROC (using Chi-squared distribution)
    # Under H0, energy follows central chi-square with N degrees of freedom
    # Under H1, energy follows non-central chi-square (or scaled central if signal is Gaussian)
    # Since our signal is Gaussian, under H1 the energy is scaled: (1+SNR)*chi2(N)
    snr_linear = 10 ** (snr_db / 10.0)
    thresh_theo = np.linspace(chi2.ppf(0.001, df=n_samples), chi2.ppf(0.999, df=n_samples) * (1 + snr_linear), 200)
    p_fa_theo = 1 - chi2.cdf(thresh_theo, df=n_samples)
    p_d_theo = 1 - chi2.cdf(thresh_theo / (1 + snr_linear), df=n_samples)

    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- Plot 1: Energy distributions and threshold ---
    ax1.hist(energies_h0, bins=50, alpha=0.6, density=True, label="H0: Noise Only", color="c")
    ax1.hist(energies_h1, bins=50, alpha=0.6, density=True, label="H1: Signal + Noise", color="r")
    
    # Choose a threshold to display
    chosen_thresh = chi2.ppf(0.95, df=n_samples)  # Threshold for Pfa = 0.05
    ax1.axvline(chosen_thresh, color="black", linestyle="--", linewidth=2, label=f"Decision Thresh (Pfa=5%)")
    
    ax1.set_title("Energy Metric Distributions (PDF)", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Received Energy (Sum of Squares)")
    ax1.set_ylabel("Probability Density")
    ax1.legend()
    ax1.grid(True, linestyle="--", alpha=0.5)

    # --- Plot 2: ROC Curves for different SNRs ---
    ax2.plot(p_fa, p_d, "o", markersize=3, label=f"Simulated ROC (SNR = {snr_db} dB)", color="r")
    ax2.plot(p_fa_theo, p_d_theo, "-", label=f"Theoretical ROC (SNR = {snr_db} dB)", color="r", linewidth=2)

    # Add ROC for other SNRs (Theoretical only for clarity)
    for snr in [-8, -2, 2]:
        snr_lin = 10 ** (snr / 10.0)
        p_d_s = 1 - chi2.cdf(thresh_theo / (1 + snr_lin), df=n_samples)
        p_fa_s = 1 - chi2.cdf(thresh_theo, df=n_samples)
        # Sort values to plot clean curves
        sort_idx = np.argsort(p_fa_s)
        ax2.plot(p_fa_s[sort_idx], p_d_s[sort_idx], "--", label=f"Theoretical ROC (SNR = {snr} dB)")

    ax2.plot([0, 1], [0, 1], "k:", label="Random Guess")
    ax2.set_title("Receiver Operating Characteristic (ROC)", fontsize=12, fontweight="bold")
    ax2.set_xlabel("Probability of False Alarm (Pfa)")
    ax2.set_ylabel("Probability of Detection (Pd)")
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.legend()

    plt.suptitle("Cognitive Radio Spectrum Sensing: Energy Detection Performance", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

    # Print detection metrics for a fixed Pfa of 5%
    idx_5pct = np.argmin(np.abs(np.array(p_fa) - 0.05))
    print("-" * 50)
    print(f"Sensing Results at threshold = {thresholds[idx_5pct]:.2f}:")
    print(f"  Target Pfa: 5.00%")
    print(f"  Simulated Pfa: {p_fa[idx_5pct]*100:.2f}%")
    print(f"  Simulated Pd:  {p_d[idx_5pct]*100:.2f}%")
    print(f"  Miss Probability (Pm): {(1-p_d[idx_5pct])*100:.2f}%")
    print("-" * 50)


if __name__ == "__main__":
    main()
