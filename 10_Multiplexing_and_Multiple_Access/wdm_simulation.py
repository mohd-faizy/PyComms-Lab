"""Wavelength Division Multiplexing (WDM) Simulation.

Simulates WDM in optical communications. Represents multiple independent data channels
modulated onto distinct wavelengths, their multiplexing onto a single fiber, and the
receiver demultiplexing process, showing channel spacing and crosstalk.
"""

import numpy as np
import matplotlib.pyplot as plt


def gaussian_pulse(f, f_center, bandwidth):
    """Represent an optical channel spectrum as a Gaussian-shaped power spectral density."""
    return np.exp(-0.5 * ((f - f_center) / (bandwidth / 2)) ** 2)


def main():
    # Frequency range in GHz (representing deviations around a center frequency, e.g. 193.1 THz)
    freq_grid = np.linspace(-300, 300, 1000)

    # WDM system parameters (ITU-T Grid: 100 GHz spacing)
    spacing = 100.0  # GHz
    channel_bandwidth = 20.0  # GHz (signal bandwidth)
    channel_centers = [-150.0, -50.0, 50.0, 150.0]  # Four channels (GHz offsets)
    channel_colors = ["r", "orange", "gray", "c"]

    # Generate individual channel spectra
    channel_spectras = []
    for fc in channel_centers:
        channel_spectras.append(gaussian_pulse(freq_grid, fc, channel_bandwidth))

    # --- Multiplexing: Summing the power spectral densities ---
    multiplexed_spectrum = np.sum(channel_spectras, axis=0)

    # --- Demultiplexing: Applying filter to extract Channel 2 (at -50 GHz) ---
    target_channel_idx = 1  # Channel 2
    fc_target = channel_centers[target_channel_idx]
    
    # Receiver optical filter (e.g. Bandpass Filter, modeled as a Gaussian filter)
    filter_bandwidth = 45.0  # GHz
    rx_filter = gaussian_pulse(freq_grid, fc_target, filter_bandwidth)

    # Demultiplexed spectrum is the product of multiplexed spectrum and filter response
    demuxed_spectrum = multiplexed_spectrum * rx_filter

    # Calculate Signal power and Crosstalk power
    # Signal is the target channel filtered
    signal_power = np.trapz(channel_spectras[target_channel_idx] * rx_filter, freq_grid)
    
    # Crosstalk is the sum of other channels leaking through the filter
    crosstalk_power = 0.0
    for idx, spec in enumerate(channel_spectras):
        if idx != target_channel_idx:
            crosstalk_power += np.trapz(spec * rx_filter, freq_grid)

    crosstalk_db = 10 * np.log10(crosstalk_power / (signal_power + 1e-12))

    # Plotting
    fig, axes = plt.subplots(3, 1, figsize=(11, 9))

    # Plot 1: Transmitter Spectra (Individual Channels)
    for idx, spec in enumerate(channel_spectras):
        axes[0].fill_between(freq_grid, 0, spec, color=channel_colors[idx], alpha=0.6, 
                             label=f"Channel {idx+1} ({fc_target + (idx-target_channel_idx)*spacing:.0f} GHz)")
    axes[0].set_title("Transmitter Channel Spectra (ITU-T 100 GHz Grid)", fontsize=11, fontweight="bold")
    axes[0].set_ylabel("Power Spectral Density")
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()

    # Plot 2: Composite Spectrum on Fiber
    axes[1].plot(freq_grid, multiplexed_spectrum, color="k", linewidth=2, label="Multiplexed Signal")
    axes[1].set_title("Composite Multiplexed Optical Spectrum inside the Fiber", fontsize=11, fontweight="bold")
    axes[1].set_ylabel("Power Spectral Density")
    axes[1].grid(True, alpha=0.3)
    axes[1].legend()

    # Plot 3: Demultiplexing & Crosstalk
    axes[2].plot(freq_grid, multiplexed_spectrum, "--", color="gray", alpha=0.5, label="Composite Input")
    axes[2].plot(freq_grid, rx_filter, ":", color="gray", linewidth=2, label="Rx Demux Filter")
    axes[2].fill_between(freq_grid, 0, demuxed_spectrum, color=channel_colors[target_channel_idx], alpha=0.7, 
                         label=f"Demuxed Channel {target_channel_idx+1}")
    # Draw crosstalk shading
    other_channels_spectrum = sum(channel_spectras[i] for i in range(len(channel_centers)) if i != target_channel_idx)
    crosstalk_spectrum = other_channels_spectrum * rx_filter
    axes[2].fill_between(freq_grid, 0, crosstalk_spectrum, color="red", alpha=0.3, label="Adjacent Channel Leakage (Crosstalk)")

    axes[2].set_title(f"Demultiplexing Channel {target_channel_idx+1} (Filter BW: {filter_bandwidth} GHz)", fontsize=11, fontweight="bold")
    axes[2].set_xlabel("Frequency Deviation (GHz)")
    axes[2].set_ylabel("Power Spectral Density")
    axes[2].grid(True, alpha=0.3)
    axes[2].legend()

    plt.suptitle("Wavelength Division Multiplexing (WDM) System Analysis", fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.show()

    # Output stats
    print("=== WDM Demultiplexing Analysis ===")
    print(f"Demux Target Channel: Channel {target_channel_idx+1}")
    print(f"Rx Filter Bandwidth:  {filter_bandwidth} GHz")
    print(f"Crosstalk Power:      {crosstalk_power:.4e}")
    print(f"Signal Power:         {signal_power:.4e}")
    print(f"Inter-Channel Crosstalk: {crosstalk_db:.2f} dB")


if __name__ == "__main__":
    main()
