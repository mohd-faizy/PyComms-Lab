"""Shannon Channel Capacity of AWGN Channel.

Visualises the Shannon-Hartley channel capacity limits.
Plots spectral efficiency (C/B) vs SNR, and the classic Shannon limit boundary
(C/B vs Eb/N0) separating achievable and unachievable transmission regions.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    # --- Plot 1: Spectral Efficiency C/B vs SNR ---
    snr_db = np.linspace(-10, 30, 400)
    snr_linear = 10 ** (snr_db / 10.0)
    spectral_efficiency = np.log2(1.0 + snr_linear)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    ax1.plot(snr_db, spectral_efficiency, label="Shannon Capacity Limit", color="gray", linewidth=2.5)
    ax1.set_title("Spectral Efficiency vs. Channel SNR", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Signal-to-Noise Ratio SNR (dB)")
    ax1.set_ylabel("Spectral Efficiency C/B (bps/Hz)")
    ax1.grid(True, which="both", linestyle="--", alpha=0.5)

    # Shading Achievable vs Unachievable regions
    ax1.fill_between(snr_db, 0, spectral_efficiency, facecolor="gray", alpha=0.2, label="Achievable Region")
    ax1.fill_between(snr_db, spectral_efficiency, 12, facecolor="r", alpha=0.1, label="Unachievable Region")
    ax1.set_ylim(0, 10.5)
    ax1.legend(loc="upper left")

    # --- Plot 2: Shannon Limit Boundary (C/B vs Eb/N0) ---
    # Eb/N0 = (C/B) / SNR_linear = (C/B) / (2^(C/B) - 1)
    # Let's parameterise by spectral efficiency R = C/B
    r = np.linspace(0.001, 8.0, 500)
    ebno_linear = (2.0**r - 1.0) / r
    ebno_db = 10 * np.log10(ebno_linear)

    # Plot the boundary line
    ax2.plot(ebno_db, r, label="Shannon Boundary", color="k", linewidth=2.5)
    
    # Shade regions
    ax2.fill_betweenx(r, -2.5, ebno_db, facecolor="r", alpha=0.1, label="Unachievable Region")
    ax2.fill_betweenx(r, ebno_db, 20, facecolor="gray", alpha=0.2, label="Achievable Region")

    # Ultimate Shannon Limit at R -> 0: Eb/N0 = ln(2) = -1.59 dB
    ax2.axvline(-1.59, color="r", linestyle=":", linewidth=2, label="Ultimate Shannon Limit (-1.59 dB)")
    ax2.plot(-1.59, 0.0, "ro", markersize=6)

    ax2.set_title("Spectral Efficiency vs. Bit Energy Eb/N0", fontsize=12, fontweight="bold")
    ax2.set_xlabel("Eb/N0 (dB)")
    ax2.set_ylabel("Spectral Efficiency R = C/B (bps/Hz)")
    ax2.set_xlim(-2.5, 15)
    ax2.set_ylim(0, 8)
    ax2.grid(True, which="both", linestyle="--", alpha=0.5)
    ax2.legend(loc="lower right")

    plt.suptitle("Shannon-Hartley Theorem: Channel Capacity and Coding Limits", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

    # Print summary
    print("=== Shannon Channel Capacity Limits ===")
    print(f"Ultimate Shannon Limit for Eb/N0: -1.59 dB (at spectral efficiency R -> 0)")
    print("-" * 65)
    print(f"{'Spectral Efficiency R (bps/Hz)':<30} | {'Required Eb/N0 (dB)':<20}")
    print("-" * 65)
    for r_test in [0.5, 1.0, 2.0, 4.0, 6.0]:
        eb_n0 = (2.0**r_test - 1.0) / r_test
        eb_n0_db = 10 * np.log10(eb_n0)
        print(f"{r_test:<30.1f} | {eb_n0_db:<20.2f} dB")


if __name__ == "__main__":
    main()
