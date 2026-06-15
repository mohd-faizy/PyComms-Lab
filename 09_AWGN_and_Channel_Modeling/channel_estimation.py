"""Pilot-based Channel Estimation (LS vs. MMSE).

Simulates pilot-aided channel estimation for flat fading channels.
Compares Least Squares (LS) and Minimum Mean Squared Error (MMSE) estimation
performance in terms of Mean Squared Error (MSE) across a range of SNR values.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    snr_db = np.arange(0, 31, 2)
    ls_mse = []
    mmse_mse = []

    np.random.seed(42)
    n_trials = 10000

    # True channel stats (for MMSE estimator)
    # Channel H is modeled as complex Gaussian with variance r_hh
    r_hh = 1.0  # Channel variance

    for snr in snr_db:
        snr_linear = 10 ** (snr / 10.0)
        # Noise variance
        noise_var = 1.0 / snr_linear

        ls_errors = 0
        mmse_errors = 0

        for _ in range(n_trials):
            # True channel coefficient
            h = (np.random.randn() + 1j * np.random.randn()) / np.sqrt(2) * np.sqrt(r_hh)

            # Pilot symbol (typically unit power)
            x_pilot = 1.0 + 0j

            # Received pilot symbol: y = h * x + n
            noise = (np.random.randn() + 1j * np.random.randn()) / np.sqrt(2) * np.sqrt(noise_var)
            y_pilot = h * x_pilot + noise

            # 1. Least Squares (LS) Estimator
            # H_ls = y / x
            h_ls = y_pilot / x_pilot

            # 2. MMSE Estimator
            # H_mmse = R_hh / (R_hh + sigma^2/|x|^2) * H_ls
            weight = r_hh / (r_hh + noise_var / (np.abs(x_pilot)**2))
            h_mmse = weight * h_ls

            # Calculate squared error
            ls_errors += np.abs(h - h_ls) ** 2
            mmse_errors += np.abs(h - h_mmse) ** 2

        ls_mse.append(ls_errors / n_trials)
        mmse_mse.append(mmse_errors / n_trials)

    # Plot MSE vs SNR
    plt.figure(figsize=(9, 5.5))
    plt.semilogy(snr_db, ls_mse, "o-", label="Least Squares (LS)", color="r", linewidth=2)
    plt.semilogy(snr_db, mmse_mse, "s-", label="Minimum Mean Squared Error (MMSE)", color="c", linewidth=2)
    plt.title("Channel Estimation MSE vs. SNR", fontsize=13, fontweight="bold")
    plt.xlabel("SNR (dB)")
    plt.ylabel("Mean Squared Error (MSE)")
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend()

    # Add text box describing estimators
    text_info = (
        "LS Estimator:\n"
        "  - No channel statistics required\n"
        "  - Enhances noise at low SNR\n\n"
        "MMSE Estimator:\n"
        "  - Uses noise variance & channel correlation\n"
        "  - Substantially lower MSE at low SNR"
    )
    plt.text(12, 1e-3, text_info, bbox=dict(facecolor="white", alpha=0.8, edgecolor="w"), fontsize=9)

    plt.tight_layout()
    plt.show()

    # Print comparisons
    print("=== Channel Estimation MSE Performance ===")
    print(f"{'SNR (dB)':<10} | {'LS MSE':<15} | {'MMSE MSE':<15}")
    print("-" * 45)
    for snr_val in [0, 10, 20, 30]:
        idx = np.where(snr_db == snr_val)[0][0]
        print(f"{snr_val:<10} | {ls_mse[idx]:<15.5e} | {mmse_mse[idx]:<15.5e}")


if __name__ == "__main__":
    main()
