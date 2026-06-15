"""Optical Link Power Budget Design.

Simulates and visualises power level (dBm) attenuation along a fiber optic link.
Calculates the maximum allowable fiber length based on receiver sensitivity,
connector losses, splice losses, and system margin.
"""

import numpy as np
import matplotlib.pyplot as plt


def calculate_power_profile(tx_power, attenuation_coeff, length, conn_loss, n_conn, splice_loss, splice_spacing):
    """Calculate the optical power level along the fiber link."""
    # Create distance points
    distances = np.linspace(0, length, 1000)
    power_profile = tx_power - attenuation_coeff * distances

    # Subtract splice losses (occurring every splice_spacing km)
    n_splices = int(np.floor(length / splice_spacing))
    for i in range(1, n_splices + 1):
        d_splice = i * splice_spacing
        power_profile[distances >= d_splice] -= splice_loss

    # Subtract connector losses
    # Assume half the connectors are at the start, half at the end (for simplicity)
    # Or distribute them: 1 connector at start (z=0) and 1 at end (z=L)
    # We will subtract connector loss at start and end
    # Power immediately after start connector
    power_profile -= (n_conn / 2.0) * conn_loss

    return distances, power_profile


def main():
    # Design Parameters
    tx_power = 3.0  # Transmitter output power (dBm)
    rx_sensitivity = -28.0  # Receiver sensitivity (dBm) for BER = 1e-9
    system_margin = 6.0  # System margin (dB)
    attenuation_coeff = 0.2  # Single-mode fiber attenuation (dB/km) at 1550 nm
    conn_loss = 0.5  # Loss per connector (dB)
    n_conn = 2  # Number of connectors (Tx and Rx patch panels)
    splice_loss = 0.1  # Loss per splice (dB)
    splice_spacing = 2.0  # Distance between splices (km)
    length = 80.0  # Link distance (km)

    # Calculate power profile
    distances, power_profile = calculate_power_profile(
        tx_power, attenuation_coeff, length, conn_loss, n_conn, splice_loss, splice_spacing
    )

    # End power calculation (directly at receiver, before/after last connector)
    rx_power = power_profile[-1] - (n_conn / 2.0) * conn_loss
    link_loss = tx_power - rx_power
    available_power = tx_power - rx_sensitivity - system_margin
    link_margin = rx_power - rx_sensitivity - system_margin

    # Determine maximum allowable length (attenuation-limited)
    # Total loss = alpha * L + L/splice_spacing * splice_loss + n_conn * conn_loss
    # available_loss = tx_power - rx_sensitivity - system_margin
    # L_max = (available_loss - n_conn * conn_loss) / (alpha + splice_loss / splice_spacing)
    effective_attenuation = attenuation_coeff + (splice_loss / splice_spacing)
    l_max = (tx_power - rx_sensitivity - system_margin - n_conn * conn_loss) / effective_attenuation

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(distances, power_profile, color="gray", linewidth=2.5, label="Optical Signal Power")

    # Add step indicators for connectors and splices
    # Mark Tx Power, Rx Sensitivity, and Margins
    plt.axhline(tx_power, color="green", linestyle="--", alpha=0.5, label="Transmitter Power (3 dBm)")
    plt.axhline(rx_sensitivity, color="red", linestyle="--", alpha=0.7, label="Rx Sensitivity (-28 dBm)")
    plt.axhline(rx_sensitivity + system_margin, color="orange", linestyle=":", alpha=0.7, label="Rx Threshold + Margin (-22 dBm)")

    # Plot final received point
    plt.plot(length, rx_power, "ro", markersize=8, label=f"Received Power ({rx_power:.2f} dBm)")

    plt.title(f"Optical Fiber Link Power Budget Profile (Length: {length} km)", fontsize=13, fontweight="bold")
    plt.xlabel("Transmission Distance (km)")
    plt.ylabel("Optical Power Level (dBm)")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend(loc="upper right")
    plt.ylim(rx_sensitivity - 5, tx_power + 2)

    # Annotations
    plt.text(5, rx_sensitivity + 1.0, f"Link Margin: {link_margin:.2f} dB", color="green" if link_margin >= 0 else "red", 
             fontweight="bold", bbox=dict(facecolor="white", alpha=0.8))

    plt.tight_layout()
    plt.show()

    # Print Link budget report
    print("=== OPTICAL FIBER LINK BUDGET REPORT ===")
    print(f"  Transmitter Launch Power:   {tx_power:.1f} dBm")
    print(f"  Receiver Sensitivity:       {rx_sensitivity:.1f} dBm")
    print(f"  Required System Margin:     {system_margin:.1f} dB")
    print(f"  Fiber Attenuation Coeff:    {attenuation_coeff:.2f} dB/km")
    print(f"  Connector Losses:           {n_conn} x {conn_loss:.2f} dB = {n_conn*conn_loss:.2f} dB")
    n_splices = int(np.floor(length / splice_spacing))
    print(f"  Splice Losses:              {n_splices} x {splice_loss:.2f} dB = {n_splices*splice_loss:.2f} dB")
    print("-" * 45)
    print(f"  Total Link Loss (Calculated): {link_loss:.2f} dB")
    print(f"  Received Power at Rx:        {rx_power:.2f} dBm")
    print(f"  Link Margin above Sensitivity: {link_margin:.2f} dB")
    if link_margin >= 0:
        print("  LINK STATUS: PASS (Link operates within specs)")
    else:
        print("  LINK STATUS: FAIL (Received power too low, adjust parameters!)")
    print(f"  Max Attenuation-limited Distance: {l_max:.2f} km")


if __name__ == "__main__":
    main()
