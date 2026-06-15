"""Wireless Receiver Diversity Combining Techniques.

Simulates Selection Combining (SC), Equal Gain Combining (EGC), and Maximal Ratio
Combining (MRC) for SIMO channels under Rayleigh fading. Plots the SNR cumulative
distribution function (CDF) to show diversity gains.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    n_trials = 50000
    snr_db = 10.0  # Average channel SNR
    snr_linear = 10 ** (snr_db / 10.0)

    # Let's simulate up to M = 4 receiver antennas
    m_antennas = [1, 2, 4]

    np.random.seed(42)

    # Dictionary to store SNR values for plotting
    snr_results = {
        "Single (M=1)": [],
        "Selection (M=2)": [],
        "Selection (M=4)": [],
        "EGC (M=2)": [],
        "EGC (M=4)": [],
        "MRC (M=2)": [],
        "MRC (M=4)": []
    }

    for trial in range(n_trials):
        # Generate independent Rayleigh fading channel coefficients
        # H is complex Gaussian: CN(0, 1)
        h = (np.random.randn(4) + 1j * np.random.randn(4)) / np.sqrt(2)
        h_amps = np.abs(h)

        # Noise power (normalized to 1)
        # Instantaneous SNR for each branch: gamma_i = |h_i|^2 * SNR_average
        gamma_branches = (h_amps ** 2) * snr_linear

        # --- M=1 (Single antenna reference) ---
        snr_results["Single (M=1)"].append(gamma_branches[0])

        # --- Selection Combining (SC) ---
        # Selects branch with maximum SNR
        snr_results["Selection (M=2)"].append(np.max(gamma_branches[:2]))
        snr_results["Selection (M=4)"].append(np.max(gamma_branches[:4]))

        # --- Equal Gain Combining (EGC) ---
        # Co-phases signals and sums them with equal weight
        # Output SNR = (sum(|h_i|))^2 * SNR_average / M
        egc_snr_2 = (np.sum(h_amps[:2])) ** 2 * snr_linear / 2.0
        egc_snr_4 = (np.sum(h_amps[:4])) ** 2 * snr_linear / 4.0
        snr_results["EGC (M=2)"].append(egc_snr_2)
        snr_results["EGC (M=4)"].append(egc_snr_4)

        # --- Maximal Ratio Combining (MRC) ---
        # Co-phases and weighs signals proportional to channel amplitude
        # Output SNR = sum(|h_i|^2) * SNR_average = sum(gamma_i)
        snr_results["MRC (M=2)"].append(np.sum(gamma_branches[:2]))
        snr_results["MRC (M=4)"].append(np.sum(gamma_branches[:4]))

    # Convert results to dB
    for key in snr_results:
        snr_results[key] = 10 * np.log10(np.array(snr_results[key]) + 1e-12)

    # Plot CDF of SNR for each technique
    plt.figure(figsize=(10, 6.5))

    colors = {
        "Single (M=1)": "gray",
        "Selection (M=2)": "orange",
        "Selection (M=4)": "orange",
        "EGC (M=2)": "c",
        "EGC (M=4)": "gray",
        "MRC (M=2)": "gray",
        "MRC (M=4)": "gray"
    }

    styles = {
        "Single (M=1)": "-",
        "Selection (M=2)": "--",
        "Selection (M=4)": "-.",
        "EGC (M=2)": "--",
        "EGC (M=4)": "-.",
        "MRC (M=2)": "--",
        "MRC (M=4)": "-."
    }

    for label, data in snr_results.items():
        # Sort data to plot CDF
        sorted_data = np.sort(data)
        cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
        plt.plot(sorted_data, cdf, label=label, color=colors[label], linestyle=styles[label], linewidth=2)

    # Threshold line for Outage Probability analysis (e.g. at 5 dB SNR)
    plt.axvline(5.0, color="red", linestyle=":", label="Outage Threshold (5 dB)")

    plt.title("SNR Cumulative Distribution Function (CDF) for Diversity Combining", fontsize=13, fontweight="bold")
    plt.xlabel("Received Instantaneous SNR (dB)")
    plt.ylabel("Cumulative Probability (Pr[SNR < x])")
    plt.xlim(-10, 25)
    plt.ylim(0, 1.0)
    plt.grid(True, which="both", linestyle="--", alpha=0.4)
    plt.legend(loc="upper left")

    plt.tight_layout()
    plt.show()

    # Print Outage Probability (Probability that SNR drops below 5 dB)
    print("=== Outage Probability (Pr[SNR < 5 dB]) ===")
    for label, data in snr_results.items():
        outage = np.mean(data < 5.0)
        print(f"  {label:<20} : {outage*100:.3f}%")


if __name__ == "__main__":
    main()
