"""Massive MIMO Beamforming and Precoding Simulation.

Simulates Maximum Ratio Transmission (MRT), Zero Forcing (ZF), and MMSE precoding
schemes in multi-user Massive MIMO systems, illustrating the effect of BS antenna scaling
on sum rate and beam directivity.
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_channel(M, K):
    """Generate Rayleigh fading channel matrix H of size K x M.

    M: number of BS antennas
    K: number of single-antenna users
    """
    # H represents the channel coefficients (complex Gaussian)
    return (np.random.randn(K, M) + 1j * np.random.randn(K, M)) / np.sqrt(2)


def get_precoder(H, snr_linear, scheme):
    """Calculate the precoding matrix W of size M x K based on the channel H.

    Normalized so that trace(W * W^H) = P_tx (total power)
    """
    K, M = H.shape
    if scheme == "MRT":
        # MRT / Conjugate Beamforming is the Hermitian transpose of H
        W = H.conj().T
    elif scheme == "ZF":
        # ZF is the pseudo-inverse of H: H^H * (H * H^H)^-1
        HH = H.conj().T
        W = HH @ np.linalg.inv(H @ HH)
    elif scheme == "MMSE":
        # MMSE is H^H * (H * H^H + (K / SNR) * I)^-1
        HH = H.conj().T
        reg = (K / snr_linear) * np.eye(K)
        W = HH @ np.linalg.inv(H @ HH + reg)
    else:
        raise ValueError("Unknown scheme")

    # Normalize power constraint: trace(W_norm * W_norm^H) = 1 (or total power)
    # We normalize each user's precoder to have equal power or overall power.
    # Standard: trace(W * W^H) = 1
    power = np.trace(W @ W.conj().T)
    W_norm = W / np.sqrt(power)
    return W_norm


def calculate_sum_rate(H, W, snr_linear):
    """Calculate the sum rate of the system in bits/s/Hz."""
    K, _ = H.shape
    rates = []
    # Received signal: y = H * W * x + n
    # For user k: y_k = H_k * W_k * x_k + sum_{i!=k} H_k * W_i * x_i + n_k
    HW = H @ W
    
    for k in range(K):
        signal_power = np.abs(HW[k, k]) ** 2 * snr_linear
        interference_power = np.sum(np.abs(HW[k, :]) ** 2) - np.abs(HW[k, k]) ** 2
        interference_power *= snr_linear
        sinr = signal_power / (interference_power + 1.0)
        rates.append(np.log2(1 + sinr))
        
    return np.sum(rates)


def main():
    K = 8  # Number of users
    snr_db = 10
    snr_linear = 10 ** (snr_db / 10.0)
    m_range = np.arange(16, 257, 16)  # BS antennas from 16 to 256

    mrt_rates = []
    zf_rates = []
    mmse_rates = []

    np.random.seed(42)

    for M in m_range:
        mrt_run, zf_run, mmse_run = [], [], []
        # Run average over channels
        for _ in range(50):
            H = generate_channel(M, K)
            
            W_mrt = get_precoder(H, snr_linear, "MRT")
            W_zf = get_precoder(H, snr_linear, "ZF")
            W_mmse = get_precoder(H, snr_linear, "MMSE")
            
            mrt_run.append(calculate_sum_rate(H, W_mrt, snr_linear))
            zf_run.append(calculate_sum_rate(H, W_zf, snr_linear))
            mmse_run.append(calculate_sum_rate(H, W_mmse, snr_linear))
            
        mrt_rates.append(np.mean(mrt_run))
        zf_rates.append(np.mean(zf_run))
        mmse_rates.append(np.mean(mmse_run))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- Plot 1: Sum Rate vs BS Antennas ---
    ax1.plot(m_range, mrt_rates, "o-", label="MRT (Conjugate Beamforming)", color="r", linewidth=2)
    ax1.plot(m_range, zf_rates, "s-", label="Zero Forcing (ZF)", color="c", linewidth=2)
    ax1.plot(m_range, mmse_rates, "^-", label="MMSE Precoding", color="gray", linewidth=2)
    ax1.set_title("Sum Rate vs. Number of BS Antennas (M)", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Number of BS Antennas (M)")
    ax1.set_ylabel("Spectral Efficiency (bits/sec/Hz)")
    ax1.grid(True, linestyle="--", alpha=0.5)
    ax1.legend()

    # --- Plot 2: Beamforming Radiation Pattern (Spatial Directivity) ---
    # Visualise the array factor / beam direction from a Uniform Linear Array (ULA) of M=32 antennas
    M_bf = 32
    theta = np.linspace(-np.pi/2, np.pi/2, 360)
    # Assume 3 user angles (in radians)
    user_angles = np.array([-np.pi/6, 0.0, np.pi/4])
    
    # Steering vectors for users: a(theta) = [1, e^(j*pi*sin(theta)), ..., e^(j*(M-1)*pi*sin(theta))]^T
    H_bf = np.zeros((len(user_angles), M_bf), dtype=complex)
    for i, angle in enumerate(user_angles):
        H_bf[i, :] = np.exp(1j * np.pi * np.arange(M_bf) * np.sin(angle))
        
    # Get ZF Precoder to separate the users spatially
    W_bf = get_precoder(H_bf, snr_linear, "ZF")
    
    # Calculate radiation pattern for each precoder column (each user's beam)
    for idx in range(len(user_angles)):
        w = W_bf[:, idx]
        pattern = []
        for th in theta:
            a = np.exp(1j * np.pi * np.arange(M_bf) * np.sin(th))
            pattern.append(np.abs(np.dot(a.conj(), w)) ** 2)
        pattern = 10 * np.log10(np.array(pattern) + 1e-6)
        # Normalize
        pattern -= np.max(pattern)
        
        ax2.plot(np.degrees(theta), pattern, label=f"Beam for User {idx+1} ({np.degrees(user_angles[idx]):.0f} deg)", linewidth=2)

    # Mark user directions
    for idx, angle in enumerate(user_angles):
        ax2.axvline(np.degrees(angle), color="grey", linestyle="--", alpha=0.7)
        ax2.text(np.degrees(angle) + 1, -5, f"User {idx+1}", rotation=90, fontsize=9, fontweight="bold")
        
    ax2.set_title(f"Zero Forcing Spatial Beamforming (ULA, M={M_bf} Antennas)", fontsize=12, fontweight="bold")
    ax2.set_xlabel("Spatial Angle (degrees)")
    ax2.set_ylabel("Normalized Array Gain (dB)")
    ax2.set_ylim(-30, 2)
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.legend()

    plt.suptitle("Massive MIMO Multi-User Beamforming & Spectral Efficiency", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

    print("=== Massive MIMO Performance Summary ===")
    print(f"Number of Users (K): {K}")
    print(f"SNR: {snr_db} dB")
    print("-" * 55)
    print(f"{'Antennas (M)':<15} | {'MRT Rate':<10} | {'ZF Rate':<10} | {'MMSE Rate':<10}")
    print("-" * 55)
    for i, M in enumerate([16, 64, 128, 256]):
        idx = np.where(m_range == M)[0][0]
        print(f"{M:<15} | {mrt_rates[idx]:<10.2f} | {zf_rates[idx]:<10.2f} | {mmse_rates[idx]:<10.2f}")


if __name__ == "__main__":
    main()
