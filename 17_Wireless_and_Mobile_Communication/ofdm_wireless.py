"""OFDM Wireless Transmission with Cyclic Prefix.

Simulates an Orthogonal Frequency Division Multiplexing (OFDM) transmitter,
multipath channel with ISI, cyclic prefix insertion, and single-tap frequency domain
equalization (FEQ). Visualises constellation diagrams before and after equalization.
"""

import numpy as np
import matplotlib.pyplot as plt


def qpsk_modulate(bits):
    """Modulate binary bits to QPSK symbols: 00->1+j, 01->-1+j, 11->-1-j, 10->1-j."""
    # Group into pairs
    reshaped = bits.reshape(-1, 2)
    symbols = (2 * reshaped[:, 0] - 1) + 1j * (2 * reshaped[:, 1] - 1)
    return symbols / np.sqrt(2)  # Normalise power to 1


def qpsk_demodulate(symbols):
    """Demodulate QPSK symbols back to binary bits."""
    real_bits = (symbols.real > 0).astype(int)
    imag_bits = (symbols.imag > 0).astype(int)
    bits = np.stack((real_bits, imag_bits), axis=-1).flatten()
    return bits


def main():
    n_subcarriers = 64
    cp_length = 16
    n_ofdm_symbols = 20
    n_bits = n_subcarriers * 2 * n_ofdm_symbols  # 2 bits per symbol for QPSK

    # Generate random data
    np.random.seed(42)
    tx_bits = np.random.randint(0, 2, n_bits)
    tx_symbols = qpsk_modulate(tx_bits)

    # Reshape into OFDM symbol grid (subcarriers x ofdm_symbols)
    tx_grid = tx_symbols.reshape(n_subcarriers, n_ofdm_symbols)

    # --- OFDM Transmitter ---
    # 1. IFFT along each column (frequency to time domain)
    tx_time = np.fft.ifft(tx_grid, axis=0) * np.sqrt(n_subcarriers)

    # 2. Add Cyclic Prefix (CP)
    # Copy last cp_length samples of each symbol to the front
    cp = tx_time[-cp_length:, :]
    tx_ofdm_frame = np.vstack((cp, tx_time))

    # Flatten the frame to transmit as a continuous time-domain signal
    tx_serial = tx_ofdm_frame.flatten(order="F")

    # --- Wireless Channel ---
    # Multipath channel with 3 taps (causes frequency-selective fading / ISI)
    h_channel = np.array([1.0, 0.4 + 0.3j, 0.1 - 0.2j])
    h_channel /= np.linalg.norm(h_channel)  # Normalize channel energy

    rx_serial_clean = np.convolve(tx_serial, h_channel, mode="full")[:len(tx_serial)]

    # Add AWGN Noise
    snr_db = 20
    signal_power = np.mean(np.abs(rx_serial_clean) ** 2)
    noise_power = signal_power / (10 ** (snr_db / 10.0))
    noise = (np.random.randn(len(rx_serial_clean)) + 1j * np.random.randn(len(rx_serial_clean))) * np.sqrt(noise_power / 2.0)
    rx_serial = rx_serial_clean + noise

    # --- OFDM Receiver ---
    # Reshape serial back into parallel OFDM symbol frames
    symbol_length_with_cp = n_subcarriers + cp_length
    rx_frame = rx_serial.reshape(symbol_length_with_cp, n_ofdm_symbols, order="F")

    # 1. Remove Cyclic Prefix
    rx_time = rx_frame[cp_length:, :]

    # 2. FFT along each column (time back to frequency domain)
    rx_grid = np.fft.fft(rx_time, axis=0) / np.sqrt(n_subcarriers)

    # --- Channel Estimation and Frequency Domain Equalization (FEQ) ---
    # Compute true channel frequency response
    h_freq = np.fft.fft(h_channel, n_subcarriers)

    # Apply 1-tap FEQ: Y_eq = Y / H_freq
    # We do this for each subcarrier across all OFDM symbols
    rx_grid_equalized = np.zeros_like(rx_grid)
    for i in range(n_ofdm_symbols):
        rx_grid_equalized[:, i] = rx_grid[:, i] / h_freq

    # Flatten symbols for constellation plotting
    rx_symbols_uneq = rx_grid.flatten()
    rx_symbols_eq = rx_grid_equalized.flatten()

    # Demodulate and calculate BER
    rx_bits = qpsk_demodulate(rx_symbols_eq)
    ber = np.mean(tx_bits != rx_bits)

    # Plotting Constellation Diagrams
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    ax1.plot(rx_symbols_uneq.real, rx_symbols_uneq.imag, "o", color="r", alpha=0.7, markersize=4)
    ax1.plot(tx_symbols.real, tx_symbols.imag, "kx", markersize=10, markeredgewidth=2, label="Tx QPSK reference")
    ax1.set_title("Constellation BEFORE Equalization\n(Distorted by Multipath Channel)", fontsize=11, fontweight="bold")
    ax1.set_xlabel("In-Phase")
    ax1.set_ylabel("Quadrature")
    ax1.grid(True, linestyle="--", alpha=0.5)
    ax1.set_xlim(-1.8, 1.8)
    ax1.set_ylim(-1.8, 1.8)
    ax1.legend()

    ax2.plot(rx_symbols_eq.real, rx_symbols_eq.imag, "o", color="gray", alpha=0.7, markersize=4)
    ax2.plot(tx_symbols.real, tx_symbols.imag, "kx", markersize=10, markeredgewidth=2, label="Tx QPSK reference")
    ax2.set_title(f"Constellation AFTER 1-Tap FEQ\n(BER = {ber*100:.2f}%)", fontsize=11, fontweight="bold")
    ax2.set_xlabel("In-Phase")
    ax2.set_ylabel("Quadrature")
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.set_xlim(-1.8, 1.8)
    ax2.set_ylim(-1.8, 1.8)
    ax2.legend()

    plt.suptitle(f"OFDM Simulation: Combating Multipath Channel at SNR = {snr_db} dB", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

    print("=== OFDM Simulation Summary ===")
    print(f"Subcarriers:     {n_subcarriers}")
    print(f"CP Length:       {cp_length}")
    print(f"Total Symbols:   {len(rx_symbols_eq)}")
    print(f"Bit Error Rate:  {ber*100:.4f}%")


if __name__ == "__main__":
    main()
