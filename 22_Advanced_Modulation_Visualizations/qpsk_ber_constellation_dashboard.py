from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc


QPSK_MAP = {
    (0, 0): (1 + 1j) / np.sqrt(2),
    (0, 1): (-1 + 1j) / np.sqrt(2),
    (1, 1): (-1 - 1j) / np.sqrt(2),
    (1, 0): (1 - 1j) / np.sqrt(2),
}


def qpsk_modulate(bits):
    pairs = bits.reshape(-1, 2)
    return np.array([QPSK_MAP[tuple(pair)] for pair in pairs])


def qpsk_demodulate(symbols):
    ideal_symbols = np.array(list(QPSK_MAP.values()))
    ideal_bits = list(QPSK_MAP.keys())
    decoded = []
    for symbol in symbols:
        index = np.argmin(np.abs(symbol - ideal_symbols))
        decoded.extend(ideal_bits[index])
    return np.array(decoded, dtype=np.uint8)


def add_awgn_for_ebn0(symbols, ebn0_db, rng):
    ebn0_linear = 10 ** (ebn0_db / 10)
    noise = np.sqrt(1 / (4 * ebn0_linear)) * (
        rng.normal(size=symbols.size) + 1j * rng.normal(size=symbols.size)
    )
    return symbols + noise


def save_dashboard(fig, filename):
    candidates = [
        Path(__file__).resolve().parent / "outputs" / filename,
        Path("C:/tmp") / filename,
    ]
    errors = []

    for output_file in candidates:
        try:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            fig.savefig(output_file, dpi=150, bbox_inches="tight")
            print(f"Saved dashboard to {output_file}")
            return
        except OSError as exc:
            errors.append(f"{output_file}: {exc}")

    print("Dashboard could not be saved automatically.")
    for error in errors:
        print(f"  {error}")


def main():
    rng = np.random.default_rng(303)
    ebn0_db = np.arange(0, 13)
    bits = rng.integers(0, 2, 100_000, dtype=np.uint8)
    symbols = qpsk_modulate(bits)
    simulated_ber = []

    for value in ebn0_db:
        received = add_awgn_for_ebn0(symbols, value, rng)
        detected = qpsk_demodulate(received)
        simulated_ber.append(np.mean(detected != bits))

    theoretical_ber = 0.5 * erfc(np.sqrt(10 ** (ebn0_db / 10)))
    low_snr_rx = add_awgn_for_ebn0(symbols[:2500], 4, rng)
    high_snr_rx = add_awgn_for_ebn0(symbols[:2500], 12, rng)

    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    axes[0, 0].scatter(low_snr_rx.real, low_snr_rx.imag, s=8, alpha=0.45)
    axes[0, 0].set_title("QPSK Received Constellation at Eb/N0 = 4 dB")
    axes[0, 1].scatter(high_snr_rx.real, high_snr_rx.imag, s=8, alpha=0.45, color="C2")
    axes[0, 1].set_title("QPSK Received Constellation at Eb/N0 = 12 dB")

    for ax in axes[0]:
        ax.axhline(0, color="black", linewidth=0.8)
        ax.axvline(0, color="black", linewidth=0.8)
        ax.set_xlabel("In-phase")
        ax.set_ylabel("Quadrature")
        ax.axis("equal")
        ax.grid(True)

    axes[1, 0].semilogy(ebn0_db, simulated_ber, "o-", label="Simulated")
    axes[1, 0].semilogy(ebn0_db, theoretical_ber, "s--", label="Theoretical")
    axes[1, 0].set_title("QPSK BER vs Eb/N0")
    axes[1, 0].set_xlabel("Eb/N0 (dB)")
    axes[1, 0].set_ylabel("BER")
    axes[1, 0].grid(True, which="both")
    axes[1, 0].legend()

    sample_symbols = symbols[:20]
    i_values = np.repeat(sample_symbols.real, 20)
    q_values = np.repeat(sample_symbols.imag, 20)
    axes[1, 1].plot(i_values, label="I branch")
    axes[1, 1].plot(q_values, label="Q branch")
    axes[1, 1].set_title("QPSK Baseband I/Q Symbol Stream")
    axes[1, 1].set_xlabel("Sample")
    axes[1, 1].set_ylabel("Amplitude")
    axes[1, 1].grid(True)
    axes[1, 1].legend()

    fig.tight_layout()
    print(f"BER at 8 dB Eb/N0: {simulated_ber[8]:.6f}")
    save_dashboard(fig, "qpsk_ber_constellation_dashboard.png")
    plt.show()


if __name__ == "__main__":
    main()
