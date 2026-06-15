"""Optical Fiber Dispersion Analysis.

Simulates chromatic dispersion in single-mode optical fibers, showing the
components (material and waveguide dispersion) across wavelengths (1.0 to 1.7 um)
and visualises pulse broadening of a Gaussian optical pulse over distance.
"""

import numpy as np
import matplotlib.pyplot as plt


def chromatic_dispersion(wavelengths_nm):
    """Approximate material and waveguide dispersion for standard SMF (G.652).

    wavelengths_nm: array of wavelengths in nm
    Returns D_material, D_waveguide, D_chromatic in ps/(nm*km)
    """
    # Material dispersion approximation
    # D_m ~ (S_0 / 4) * (lambda - lambda_0^4 / lambda^3)
    # where S_0 is zero-dispersion slope (~0.09 ps/(nm^2*km)), lambda_0 = 1312 nm
    s0 = 0.09
    l0 = 1312.0
    d_mat = (s0 / 4.0) * (wavelengths_nm - (l0**4) / (wavelengths_nm**3))

    # Waveguide dispersion approximation (always negative in this range)
    # D_w ~ -4 to -8 ps/(nm*km) around 1550nm
    # Let's model D_w as a slow curve decreasing with wavelength
    d_wg = -5.0 * (1.5 - (wavelengths_nm - 1312) / 800)

    d_chrom = d_mat + d_wg
    return d_mat, d_wg, d_chrom


def main():
    wavelengths = np.linspace(1000, 1700, 500)
    d_mat, d_wg, d_chrom = chromatic_dispersion(wavelengths)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- Plot 1: Dispersion vs. Wavelength ---
    ax1.plot(wavelengths, d_mat, "--", label="Material Dispersion ($D_m$)", color="orange")
    ax1.plot(wavelengths, d_wg, ":", label="Waveguide Dispersion ($D_w$)", color="c")
    ax1.plot(wavelengths, d_chrom, "-", label="Chromatic Dispersion ($D_c = D_m + D_w$)", color="k", linewidth=2.5)

    # Highlight key wavelengths
    # 1310 nm Zero dispersion
    idx_zero = np.argmin(np.abs(d_chrom))
    lambda_zero = wavelengths[idx_zero]
    ax1.plot(lambda_zero, 0.0, "ro", markersize=6)
    ax1.axhline(0, color="grey", linewidth=0.8)
    ax1.text(lambda_zero - 80, 5, fr"$\lambda_0 \approx {lambda_zero:.0f}$ nm", color="red", fontweight="bold")

    # 1550 nm Minimum loss window
    idx_1550 = np.argmin(np.abs(wavelengths - 1550))
    ax1.axvline(1550, color="green", linestyle="--", alpha=0.5)
    ax1.text(1555, -15, "1550 nm Window\n(Min. Loss, High Disp.)", color="green", fontsize=9)
    ax1.plot(1550, d_chrom[idx_1550], "go")

    ax1.set_title("Optical Fiber Dispersion vs. Wavelength", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Wavelength (nm)")
    ax1.set_ylabel(r"Dispersion Parameter $D$ [ps/(nm$\cdot$km)]")
    ax1.set_ylim(-35, 25)
    ax1.grid(True, linestyle="--", alpha=0.5)
    ax1.legend()

    # --- Plot 2: Pulse Broadening over Distance ---
    # Model a Gaussian optical pulse: P(t) = exp(-t^2 / (2 * sigma_0^2))
    # Broadened pulse width: sigma_z = sqrt(sigma_0^2 + (D * z * sigma_lambda)^2)
    t_grid = np.linspace(-100, 100, 1000)  # in picoseconds
    sigma_0 = 10.0  # Initial pulse width (rms) = 10 ps
    src_spectral_width = 1.0  # Source spectral width delta_lambda = 1.0 nm
    d_val = d_chrom[idx_1550]  # Dispersion at 1550 nm (~ 17 ps/(nm*km))

    distances_km = [0, 10, 30, 50]
    colors = ["gray", "c", "gray", "r"]

    for dist, col in zip(distances_km, colors):
        # Broadened pulse standard deviation
        sigma_z = np.sqrt(sigma_0**2 + (d_val * dist * src_spectral_width)**2)
        # Normalised pulse power profile
        pulse = (sigma_0 / sigma_z) * np.exp(-0.5 * (t_grid / sigma_z)**2)
        
        ax2.plot(t_grid, pulse, label=f"Distance = {dist} km (rms = {sigma_z:.1f} ps)", color=col, linewidth=2)

    ax2.set_title("Gaussian Pulse Broadening in Time (at 1550 nm)", fontsize=12, fontweight="bold")
    ax2.set_xlabel("Time (picoseconds)")
    ax2.set_ylabel("Normalized Optical Power")
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.legend()

    plt.suptitle("Chromatic Dispersion & Pulse Broadening in Single-Mode Fiber", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

    # Print summary
    print("=== Dispersion Characteristics at 1550 nm ===")
    print(f"  Dispersion Parameter (D_c): {d_val:.2f} ps/(nm*km)")
    print(f"  Initial pulse RMS width:    {sigma_0} ps")
    print(f"  Source spectral width:      {src_spectral_width} nm")
    for d in [10, 30, 50]:
        sig_z = np.sqrt(sigma_0**2 + (d_val * d * src_spectral_width)**2)
        expansion = sig_z / sigma_0
        print(f"  At {d:<2} km -> Pulse RMS width = {sig_z:.2f} ps (expanded by {expansion:.2f}x)")


if __name__ == "__main__":
    main()
