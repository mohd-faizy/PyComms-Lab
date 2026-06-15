"""Complete baseband digital transmission system.

Simulates a full Tx -> Channel -> Rx chain:
  Source bits -> Pulse shaping -> AWGN Channel -> Matched filter -> Sampling -> Decision
Reports BER for different SNR values.
"""

import numpy as np
import matplotlib.pyplot as plt


def raised_cosine_filter(beta, span, sps):
    """Root-raised-cosine FIR filter."""
    n = np.arange(-span * sps // 2, span * sps // 2 + 1)
    t = n / sps
    h = np.sinc(t)
    denom = 1 - (2 * beta * t) ** 2
    denom[np.abs(denom) < 1e-12] = 1e-12
    h *= np.cos(np.pi * beta * t) / denom
    return h / np.linalg.norm(h)


def simulate_baseband(n_bits, snr_db, sps, pulse, rng):
    """Run a single baseband simulation and return BER."""
    bits = rng.integers(0, 2, n_bits)
    symbols = 2.0 * bits - 1.0

    # Upsample and pulse-shape
    up = np.zeros(n_bits * sps)
    up[::sps] = symbols
    tx = np.convolve(up, pulse, mode="same")

    # AWGN channel
    sig_power = np.mean(tx ** 2)
    noise_power = sig_power / (10 ** (snr_db / 10))
    rx = tx + rng.normal(scale=np.sqrt(noise_power), size=tx.size)

    # Matched filter (correlator)
    mf_out = np.convolve(rx, pulse[::-1], mode="same")

    # Sample at symbol instants
    samples = mf_out[::sps][:n_bits]

    # Decision
    decoded = (samples > 0).astype(int)
    ber = np.mean(decoded != bits)
    return ber, tx, rx, mf_out, bits, decoded


def main():
    rng = np.random.default_rng(55)
    sps = 8
    pulse = raised_cosine_filter(beta=0.35, span=6, sps=sps)
    n_bits = 50000

    # BER vs SNR
    snr_range = np.arange(0, 16, 1)
    ber_values = []
    for snr in snr_range:
        ber, *_ = simulate_baseband(n_bits, snr, sps, pulse, rng)
        ber_values.append(max(ber, 1e-6))

    # Detailed run for plotting
    snr_plot = 8
    ber, tx, rx, mf_out, bits, decoded = simulate_baseband(
        200, snr_plot, sps, pulse, rng
    )

    fig, axes = plt.subplots(2, 2, figsize=(14, 8))

    # Transmitted signal
    axes[0, 0].plot(tx[:400], color="tab:blue", lw=0.8)
    axes[0, 0].set_title("Transmitted (Pulse-Shaped)")
    axes[0, 0].set_xlabel("Sample")
    axes[0, 0].grid(True)

    # Received signal
    axes[0, 1].plot(rx[:400], color="tab:orange", lw=0.8)
    axes[0, 1].set_title(f"Received (after AWGN, SNR={snr_plot} dB)")
    axes[0, 1].set_xlabel("Sample")
    axes[0, 1].grid(True)

    # Matched filter output
    axes[1, 0].plot(mf_out[:400], color="tab:green", lw=0.8)
    axes[1, 0].set_title("Matched Filter Output")
    axes[1, 0].set_xlabel("Sample")
    axes[1, 0].grid(True)

    # BER curve
    axes[1, 1].semilogy(snr_range, ber_values, "bo-", label="Simulated BER")
    axes[1, 1].set_title("BER vs SNR")
    axes[1, 1].set_xlabel("SNR (dB)")
    axes[1, 1].set_ylabel("BER")
    axes[1, 1].legend()
    axes[1, 1].grid(True, which="both")

    fig.suptitle("Complete Baseband Digital Transmission System", fontsize=13)
    fig.tight_layout()
    plt.show()

    print("=== BER Results ===")
    for snr, ber in zip(snr_range, ber_values):
        print(f"  SNR = {snr:2d} dB -> BER = {ber:.2e}")


if __name__ == "__main__":
    main()
