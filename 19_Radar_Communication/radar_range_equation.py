"""Radar range equation calculation and detection analysis.

Computes maximum detection range using the radar range equation and
plots detection probability vs range for different radar configurations.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def radar_range_equation(pt, gt, gr, wavelength, sigma, pmin):
    """Compute maximum radar range using the radar equation.

    R_max = ((Pt * Gt * Gr * lambda^2 * sigma) / ((4*pi)^3 * Pmin))^(1/4)
    """
    numerator = pt * gt * gr * wavelength ** 2 * sigma
    denominator = (4 * np.pi) ** 3 * pmin
    return (numerator / denominator) ** 0.25


def received_power(pt, gt, gr, wavelength, sigma, R):
    """Received power as a function of range."""
    return (pt * gt * gr * wavelength ** 2 * sigma) / ((4 * np.pi) ** 3 * R ** 4)


def detection_probability(snr_db, pfa=1e-6):
    """Approximation of detection probability for a given SNR and Pfa."""
    threshold = norm.isf(pfa)
    pd = norm.sf(threshold - np.sqrt(2 * 10 ** (snr_db / 10)))
    return pd


def main():
    # Radar parameters
    pt = 1e6        # peak transmit power (1 MW)
    gt = 1000       # transmit antenna gain (30 dBi)
    gr = 1000       # receive antenna gain (30 dBi)
    freq = 3e9      # operating frequency (3 GHz, S-band)
    wavelength = 3e8 / freq
    pmin = 1e-12    # minimum detectable power (-90 dBm)

    # Target RCS values (m^2)
    rcs_values = [0.1, 1.0, 10.0, 100.0]
    rcs_labels = ["Bird (0.1 m^2)", "Small UAV (1 m^2)",
                  "Fighter (10 m^2)", "Large aircraft (100 m^2)"]

    fig, axes = plt.subplots(2, 2, figsize=(14, 9))

    # --- Max range vs RCS ---
    rcs_range = np.logspace(-2, 3, 200)
    max_ranges = radar_range_equation(pt, gt, gr, wavelength, rcs_range, pmin)
    axes[0, 0].loglog(rcs_range, max_ranges / 1000, color="tab:blue", lw=2)
    for rcs, lbl in zip(rcs_values, rcs_labels):
        r = radar_range_equation(pt, gt, gr, wavelength, rcs, pmin)
        axes[0, 0].plot(rcs, r / 1000, "ro", markersize=8)
        axes[0, 0].annotate(f"{lbl}\n{r/1000:.1f} km", (rcs, r / 1000),
                           fontsize=7, textcoords="offset points",
                           xytext=(10, 5))
    axes[0, 0].set_title("Maximum Detection Range vs Target RCS")
    axes[0, 0].set_xlabel("Radar Cross Section rho (m^2)")
    axes[0, 0].set_ylabel("Range (km)")
    axes[0, 0].grid(True, which="both")

    # --- Received power vs range ---
    ranges = np.linspace(1000, 300_000, 500)
    for rcs, lbl in zip(rcs_values, rcs_labels):
        pr = received_power(pt, gt, gr, wavelength, rcs, ranges)
        pr_dbm = 10 * np.log10(pr * 1000)
        axes[0, 1].plot(ranges / 1000, pr_dbm, label=lbl)
    axes[0, 1].axhline(10 * np.log10(pmin * 1000), ls="--", color="red",
                       label="Min detectable")
    axes[0, 1].set_title("Received Power vs Range")
    axes[0, 1].set_xlabel("Range (km)")
    axes[0, 1].set_ylabel("Received Power (dBm)")
    axes[0, 1].legend(fontsize=8)
    axes[0, 1].grid(True)

    # --- Detection probability vs SNR ---
    snr_range = np.linspace(-5, 25, 200)
    for pfa in [1e-4, 1e-6, 1e-8]:
        pd = detection_probability(snr_range, pfa)
        axes[1, 0].plot(snr_range, pd, label=f"Pfa = {pfa:.0e}")
    axes[1, 0].set_title("Detection Probability vs SNR")
    axes[1, 0].set_xlabel("SNR (dB)")
    axes[1, 0].set_ylabel("P_detection")
    axes[1, 0].legend()
    axes[1, 0].grid(True)

    # --- Max range vs transmit power ---
    pt_range = np.logspace(3, 7, 200)  # 1 kW to 10 MW
    for rcs in [1.0, 10.0]:
        r_max = radar_range_equation(pt_range, gt, gr, wavelength, rcs, pmin)
        axes[1, 1].semilogx(pt_range / 1000, r_max / 1000,
                           label=f"rho = {rcs} m^2")
    axes[1, 1].set_title("Max Range vs Transmit Power")
    axes[1, 1].set_xlabel("Transmit Power (kW)")
    axes[1, 1].set_ylabel("Max Range (km)")
    axes[1, 1].legend()
    axes[1, 1].grid(True, which="both")

    fig.suptitle("Radar Range Equation Analysis", fontsize=13)
    fig.tight_layout()
    plt.show()

    print("=== Maximum Detection Ranges ===")
    for rcs, lbl in zip(rcs_values, rcs_labels):
        r = radar_range_equation(pt, gt, gr, wavelength, rcs, pmin)
        print(f"  {lbl:30s}: {r/1000:.1f} km")


if __name__ == "__main__":
    main()
