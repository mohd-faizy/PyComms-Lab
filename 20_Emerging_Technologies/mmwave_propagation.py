"""Millimeter Wave (mmWave) Propagation Characteristics.

Simulates path loss models for mmWave bands (28 GHz and 60 GHz) compared to
sub-6 GHz (2.4 GHz) in Urban Micro (UMi) environments (LOS and NLOS),
including atmospheric and oxygen absorption at 60 GHz.
"""

import numpy as np
import matplotlib.pyplot as plt


def free_space_path_loss(d, f_hz):
    """Calculate Free Space Path Loss in dB."""
    c = 3e8
    return 20 * np.log10(d) + 20 * np.log10(f_hz) + 20 * np.log10(4 * np.pi / c)


def irt_path_loss_3gpp(d, f_ghz, scenario="UMi_LOS"):
    """Calculate 3GPP TR 38.901 Path Loss in dB for Urban Micro (UMi).

    Valid for 0.5 GHz < f < 100 GHz.
    """
    if scenario == "UMi_LOS":
        # PL_UMi-LOS = 32.4 + 21*log10(d) + 20*log10(fc)
        pl = 32.4 + 21 * np.log10(d) + 20 * np.log10(f_ghz)
    elif scenario == "UMi_NLOS":
        # PL_UMi-NLOS = 22.4 + 35.3*log10(d) + 21.3*log10(fc)
        pl_los = 32.4 + 21 * np.log10(d) + 20 * np.log10(f_ghz)
        pl_nlos = 22.4 + 35.3 * np.log10(d) + 21.3 * np.log10(f_ghz)
        pl = np.maximum(pl_los, pl_nlos)
    else:
        raise ValueError("Unknown scenario")
    return pl


def main():
    distances = np.linspace(10, 1000, 500)  # 10m to 1km

    # Frequencies
    f_2_4 = 2.4e9
    f_28 = 28.0  # GHz
    f_60 = 60.0  # GHz

    # Path Loss calculations
    pl_2_4_fspl = free_space_path_loss(distances, f_2_4)
    pl_28_los = irt_path_loss_3gpp(distances, f_28, "UMi_LOS")
    pl_28_nlos = irt_path_loss_3gpp(distances, f_28, "UMi_NLOS")
    pl_60_los = irt_path_loss_3gpp(distances, f_60, "UMi_LOS")
    pl_60_nlos = irt_path_loss_3gpp(distances, f_60, "UMi_NLOS")

    # Add atmospheric attenuation (Oxygen absorption)
    # At 60 GHz, oxygen absorption is peak (~15 dB/km)
    # At 28 GHz, absorption is much lower (~0.06 dB/km)
    att_coeff_60 = 15.0 / 1000.0  # dB/meter
    att_coeff_28 = 0.06 / 1000.0  # dB/meter

    pl_60_los_att = pl_60_los + att_coeff_60 * distances
    pl_60_nlos_att = pl_60_nlos + att_coeff_60 * distances
    pl_28_los_att = pl_28_los + att_coeff_28 * distances

    # Plot results
    plt.figure(figsize=(11, 6.5))

    # Sub-6 GHz reference
    plt.plot(distances, pl_2_4_fspl, "--", label="2.4 GHz Free Space Path Loss", color="gray", linewidth=1.5)

    # 28 GHz (FR2 mmWave)
    plt.plot(distances, pl_28_los, label="28 GHz UMi - Line-of-Sight (LOS)", color="c", linewidth=2)
    plt.plot(distances, pl_28_nlos, label="28 GHz UMi - Non-LOS (NLOS)", color="gray", linewidth=2, linestyle="-.")

    # 60 GHz (unlicensed mmWave with high oxygen absorption)
    plt.plot(distances, pl_60_los, label="60 GHz UMi - LOS (No Atmos. Loss)", color="r", linewidth=1.5, alpha=0.5)
    plt.plot(distances, pl_60_los_att, label="60 GHz UMi - LOS + Oxygen Absorption (15 dB/km)", color="r", linewidth=2.5)
    plt.plot(distances, pl_60_nlos_att, label="60 GHz UMi - NLOS + Oxygen Absorption (15 dB/km)", color="gray", linewidth=2, linestyle=":")

    plt.title("Millimeter Wave (mmWave) Path Loss & Atmospheric Absorption Profiles", fontsize=13, fontweight="bold")
    plt.xlabel("Transmission Distance (meters)", fontsize=11)
    plt.ylabel("Path Loss (dB)", fontsize=11)
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend(fontsize=10, loc="lower right")

    # Add text annotation about 60 GHz oxygen absorption
    plt.text(500, 80, "Atmospheric absorption creates high isolation,\nuseful for ultra-dense, secure small cells.",
             bbox=dict(facecolor="white", alpha=0.8, edgecolor="w"), fontsize=9)

    plt.tight_layout()
    plt.show()

    # Print comparative table
    print("=== Path Loss comparison at specific distances ===")
    print(f"{'Distance':<10} | {'2.4 GHz FSPL':<15} | {'28 GHz LOS':<15} | {'28 GHz NLOS':<15} | {'60 GHz LOS+O2':<15} | {'60 GHz NLOS+O2':<15}")
    print("-" * 95)
    for dist in [50, 100, 200, 500, 1000]:
        pl_2_4 = free_space_path_loss(dist, f_2_4)
        pl_28_l = irt_path_loss_3gpp(dist, f_28, "UMi_LOS") + att_coeff_28 * dist
        pl_28_nl = irt_path_loss_3gpp(dist, f_28, "UMi_NLOS") + att_coeff_28 * dist
        pl_60_l = irt_path_loss_3gpp(dist, f_60, "UMi_LOS") + att_coeff_60 * dist
        pl_60_nl = irt_path_loss_3gpp(dist, f_60, "UMi_NLOS") + att_coeff_60 * dist
        print(f"{dist:<9}m | {pl_2_4:<13.2f} dB | {pl_28_l:<13.2f} dB | {pl_28_nl:<13.2f} dB | {pl_60_l:<13.2f} dB | {pl_60_nl:<13.2f} dB")


if __name__ == "__main__":
    main()
