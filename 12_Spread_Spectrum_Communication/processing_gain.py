"""Processing gain and jamming margin in spread spectrum systems.

Computes and visualizes processing gain (Gp) for different spreading
factors and demonstrates how it translates into jamming margin.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    # Processing gain for different chip rates / data rates
    spreading_factors = np.array([4, 8, 16, 32, 64, 128, 256, 512, 1024])
    gp_db = 10 * np.log10(spreading_factors)

    # Jamming margin analysis
    # Jm = Gp - SNR_out_required - System_losses
    snr_required_db = 10  # minimum SNR for acceptable BER
    system_loss_db = 2    # implementation losses

    jamming_margin = gp_db - snr_required_db - system_loss_db

    fig, axes = plt.subplots(2, 2, figsize=(13, 8))

    # Processing gain vs spreading factor
    axes[0, 0].semilogx(spreading_factors, gp_db, "bo-", markersize=8)
    axes[0, 0].set_title("Processing Gain vs Spreading Factor")
    axes[0, 0].set_xlabel("Spreading Factor (chips/bit)")
    axes[0, 0].set_ylabel("Processing Gain (dB)")
    axes[0, 0].grid(True, which="both")
    for sf, gp in zip(spreading_factors, gp_db):
        axes[0, 0].annotate(f"{gp:.1f} dB", (sf, gp),
                           textcoords="offset points", xytext=(5, 5),
                           fontsize=8)

    # Jamming margin
    colours = ["tab:green" if jm > 0 else "tab:red" for jm in jamming_margin]
    axes[0, 1].bar(range(len(spreading_factors)), jamming_margin,
                   tick_label=[str(s) for s in spreading_factors],
                   color=colours)
    axes[0, 1].axhline(0, color="k", lw=1)
    axes[0, 1].set_title(f"Jamming Margin (SNR_req={snr_required_db} dB, "
                         f"Loss={system_loss_db} dB)")
    axes[0, 1].set_xlabel("Spreading Factor")
    axes[0, 1].set_ylabel("Jamming Margin (dB)")
    axes[0, 1].grid(True, alpha=0.3)

    # Spectrum: narrowband vs spread
    rng = np.random.default_rng(10)
    n = 2048
    fs = 50_000
    # Narrowband signal
    data_rate = 100  # Hz (symbol rate)
    bits = 2 * rng.integers(0, 2, int(np.ceil(n * data_rate / fs))) - 1
    nb_signal = np.repeat(bits, int(fs / data_rate))[:n]
    # Spread signal (SF=32)
    sf = 32
    pn = 2 * rng.integers(0, 2, n) - 1
    spread_signal = np.repeat(bits, int(fs / data_rate))[:n] * pn[:n]

    freqs = np.fft.rfftfreq(n, 1 / fs)
    psd_nb = 10 * np.log10(np.abs(np.fft.rfft(nb_signal)) ** 2 / n + 1e-12)
    psd_sp = 10 * np.log10(np.abs(np.fft.rfft(spread_signal)) ** 2 / n + 1e-12)

    axes[1, 0].plot(freqs / 1000, psd_nb, alpha=0.7, label="Narrowband")
    axes[1, 0].plot(freqs / 1000, psd_sp, alpha=0.7, label="Spread (SF=32)")
    axes[1, 0].set_title("PSD: Narrowband vs Spread Signal")
    axes[1, 0].set_xlabel("Frequency (kHz)")
    axes[1, 0].set_ylabel("PSD (dB)")
    axes[1, 0].legend()
    axes[1, 0].grid(True)

    # Power budget diagram
    labels = ["Signal\nPower", "Processing\nGain", "Required\nSNR",
              "System\nLosses", "Jamming\nMargin"]
    sf_example = 128
    gp_ex = 10 * np.log10(sf_example)
    jm_ex = gp_ex - snr_required_db - system_loss_db
    values = [0, gp_ex, snr_required_db, system_loss_db, jm_ex]
    cumulative = [0, gp_ex, gp_ex - snr_required_db,
                  gp_ex - snr_required_db - system_loss_db, jm_ex]
    colours2 = ["tab:blue", "tab:green", "tab:orange", "tab:red", "tab:purple"]
    axes[1, 1].bar(labels, values, color=colours2, alpha=0.7, edgecolor="k")
    axes[1, 1].set_title(f"Power Budget (SF={sf_example})")
    axes[1, 1].set_ylabel("dB")
    axes[1, 1].grid(True, alpha=0.3)

    fig.suptitle("Spread Spectrum - Processing Gain & Jamming Margin", fontsize=13)
    fig.tight_layout()
    plt.show()

    print("=== Processing Gain & Jamming Margin ===")
    print(f"{'SF':>6} | {'Gp (dB)':>8} | {'Jm (dB)':>8}")
    print("-" * 30)
    for sf, gp, jm in zip(spreading_factors, gp_db, jamming_margin):
        print(f"{sf:>6} | {gp:>8.1f} | {jm:>8.1f}")


if __name__ == "__main__":
    main()
