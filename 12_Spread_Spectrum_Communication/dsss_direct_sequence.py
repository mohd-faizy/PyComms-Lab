"""Direct Sequence Spread Spectrum (DSSS) simulation.

Spreads a narrowband data signal using a PN code, transmits through an
AWGN channel, and despreads at the receiver to recover the original data.
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_pn_sequence(length, rng):
    """Generate a pseudo-random PN sequence of +/-1."""
    return 2 * rng.integers(0, 2, length) - 1


def main():
    rng = np.random.default_rng(42)
    n_bits = 20
    chips_per_bit = 16  # processing gain = 16 (12 dB)
    snr_db = -5  # very low SNR - below noise floor

    # Data bits
    data = 2 * rng.integers(0, 2, n_bits) - 1  # +/-1

    # PN code (repeated for each bit)
    pn = generate_pn_sequence(chips_per_bit, rng)
    pn_full = np.tile(pn, n_bits)

    # Spread: each bit is multiplied by the PN code
    spread = np.repeat(data, chips_per_bit) * pn_full

    # AWGN channel
    sig_power = np.mean(spread ** 2)
    noise_power = sig_power / (10 ** (snr_db / 10))
    noise = rng.normal(scale=np.sqrt(noise_power), size=spread.size)
    received = spread + noise

    # Despread: multiply by same PN code again
    despread = received * pn_full

    # Integrate and dump (sum over each chip period)
    recovered = np.array([
        despread[i * chips_per_bit:(i + 1) * chips_per_bit].sum()
        for i in range(n_bits)
    ])
    decoded = np.sign(recovered)

    ber = np.mean(decoded != data)

    fig, axes = plt.subplots(5, 1, figsize=(14, 12))

    # Original data
    t_data = np.repeat(data, chips_per_bit)
    axes[0].step(range(len(t_data)), t_data, where="post", color="tab:blue")
    axes[0].set_title("Original Data (each bit spans chip period)")
    axes[0].set_ylim(-1.5, 1.5)
    axes[0].grid(True)

    # Spread signal
    axes[1].plot(spread, lw=0.5, color="tab:orange")
    axes[1].set_title("Spread Signal (data * PN code)")
    axes[1].grid(True)

    # Received (buried in noise)
    axes[2].plot(received, lw=0.3, color="tab:red")
    axes[2].set_title(f"Received Signal (AWGN, SNR = {snr_db} dB - signal buried!)")
    axes[2].grid(True)

    # Despread
    axes[3].plot(despread, lw=0.5, color="tab:green")
    axes[3].set_title("Despread Signal (received * PN code)")
    axes[3].grid(True)

    # Recovered
    axes[4].stem(range(n_bits), recovered, linefmt="tab:purple",
                markerfmt="o", basefmt="k-")
    axes[4].axhline(0, color="k", lw=0.5)
    axes[4].set_title(f"Integrate-and-Dump Output -> BER = {ber:.3f}")
    axes[4].set_xlabel("Bit Index")
    axes[4].grid(True)

    fig.suptitle(f"DSSS - Processing Gain = {chips_per_bit} "
                 f"({10*np.log10(chips_per_bit):.1f} dB)", fontsize=13)
    fig.tight_layout()
    plt.show()

    print(f"Chips/bit (processing gain): {chips_per_bit}")
    print(f"Channel SNR: {snr_db} dB")
    print(f"Effective SNR after despreading: ~{snr_db + 10*np.log10(chips_per_bit):.1f} dB")
    print(f"BER: {ber:.4f}")


if __name__ == "__main__":
    main()
