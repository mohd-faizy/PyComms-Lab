from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


BIT_TO_LEVEL = {
    (0, 0): -3,
    (0, 1): -1,
    (1, 1): 1,
    (1, 0): 3,
}
LEVEL_TO_BITS = {level: bits for bits, level in BIT_TO_LEVEL.items()}
LEVELS = np.array([-3, -1, 1, 3])
CHANNEL_MATRIX = np.array([[11.0, 10.0], [10.0, 11.0]])
CHANNEL_INV = np.linalg.inv(CHANNEL_MATRIX)


def text_to_bits(message):
    data = np.frombuffer(message.encode("utf-8"), dtype=np.uint8)
    return np.unpackbits(data)


def bits_to_text(bits):
    usable = bits[: len(bits) - (len(bits) % 8)]
    data = np.packbits(usable).tobytes()
    return data.decode("utf-8", errors="replace")


def qam16_modulate(bits):
    padding = (-len(bits)) % 4
    if padding:
        bits = np.pad(bits, (0, padding))
    symbols = []
    for group in bits.reshape(-1, 4):
        i_level = BIT_TO_LEVEL[tuple(group[:2])]
        q_level = BIT_TO_LEVEL[tuple(group[2:])]
        symbols.append(i_level + 1j * q_level)
    return np.array(symbols), padding


def qam16_demodulate(symbols):
    decoded = []
    for symbol in symbols:
        i_level = LEVELS[np.argmin(np.abs(symbol.real - LEVELS))]
        q_level = LEVELS[np.argmin(np.abs(symbol.imag - LEVELS))]
        decoded.extend(LEVEL_TO_BITS[int(i_level)])
        decoded.extend(LEVEL_TO_BITS[int(q_level)])
    return np.array(decoded, dtype=np.uint8)


def apply_channel(symbols, noise_factor, rng):
    pairs = np.column_stack([symbols.real, symbols.imag])
    channel_output = pairs @ CHANNEL_MATRIX.T
    rms = np.sqrt(np.mean(pairs**2))
    noise = rng.normal(0, max(rms, 1.0) * noise_factor, size=channel_output.shape)
    return channel_output + noise


def equalize(channel_output):
    equalized_pairs = channel_output @ CHANNEL_INV.T
    return equalized_pairs[:, 0] + 1j * equalized_pairs[:, 1]


def similarity(original, recovered):
    return SequenceMatcher(None, original, recovered).ratio()


def save_dashboard(fig, filename):
    candidates = [
        Path(__file__).resolve().parent / "outputs" / filename,
        Path("C:/tmp") / filename,
    ]
    errors = []

    for output_file in candidates:
        try:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            fig.savefig(output_file, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
            print(f"Saved dashboard to {output_file}")
            return
        except OSError as exc:
            errors.append(f"{output_file}: {exc}")

    print("Dashboard could not be saved automatically.")
    for error in errors:
        print(f"  {error}")


def run_trial(message, noise_factor, seed=202):
    rng = np.random.default_rng(seed)
    bits = text_to_bits(message)
    tx_symbols, padding = qam16_modulate(bits)
    raw_pairs = apply_channel(tx_symbols, noise_factor, rng)
    eq_symbols = equalize(raw_pairs)
    decoded_bits = qam16_demodulate(eq_symbols)

    if padding:
        decoded_bits = decoded_bits[:-padding]
    decoded_bits = decoded_bits[: bits.size]
    recovered = bits_to_text(decoded_bits)
    return tx_symbols, raw_pairs, eq_symbols, recovered, similarity(message, recovered)


def draw_dashboard(message, noise_factors, results):
    ideal = np.array([i + 1j * q for i in LEVELS for q in LEVELS])
    mid_noise = 0.8 if 0.8 in results else noise_factors[len(noise_factors) // 2]
    tx_symbols, raw_pairs, mid_equalized, _, _ = results[mid_noise]
    similarities = [results[nf][4] for nf in noise_factors]

    fig = plt.figure(figsize=(18, 12), facecolor="w")
    fig.suptitle(
        "16-QAM Modulation / Demodulation - Visualization Dashboard",
        fontsize=18,
        fontweight="bold",
        y=0.98,
        color="k",
    )
    grid = gridspec.GridSpec(2, 3, hspace=0.35, wspace=0.32)

    ax1 = fig.add_subplot(grid[0, 0])
    ax1.scatter(ideal.real, ideal.imag, marker="s", s=120, c="gray", edgecolors="gray", label="Ideal symbols")
    for point in ideal:
        ax1.annotate(f"({int(point.real)},{int(point.imag)})", (point.real, point.imag), fontsize=7, ha="center", xytext=(0, 7), textcoords="offset points")
    ax1.axhline(0, color="gray", linewidth=0.7)
    ax1.axvline(0, color="gray", linewidth=0.7)
    ax1.set_title("Ideal 16-QAM Constellation", fontweight="bold")
    ax1.set_xlabel("In-phase (I)")
    ax1.set_ylabel("Quadrature (Q)")
    ax1.set_xlim(-5, 5)
    ax1.set_ylim(-5, 5)
    ax1.set_aspect("equal")
    ax1.grid(True, alpha=0.25)
    ax1.legend()

    ax2 = fig.add_subplot(grid[0, 1])
    ax2.scatter(ideal.real, ideal.imag, marker="s", s=90, c="gray", edgecolors="gray", label="Ideal")
    ax2.scatter(mid_equalized.real, mid_equalized.imag, s=28, c="r", alpha=0.55, label=f"Received noise={mid_noise}")
    ax2.axhline(0, color="gray", linewidth=0.7)
    ax2.axvline(0, color="gray", linewidth=0.7)
    ax2.set_title(f"Received Constellation after Equalization (noise={mid_noise})", fontweight="bold")
    ax2.set_xlabel("In-phase (I)")
    ax2.set_ylabel("Quadrature (Q)")
    ax2.set_xlim(-7, 7)
    ax2.set_ylim(-7, 7)
    ax2.set_aspect("equal")
    ax2.grid(True, alpha=0.25)
    ax2.legend()

    ax3 = fig.add_subplot(grid[0, 2])
    ax3.plot(noise_factors, similarities, "o-", color="gray", linewidth=2.5, markerfacecolor="orange")
    ax3.fill_between(noise_factors, similarities, alpha=0.15, color="gray")
    ax3.set_title("Recovered Text Similarity vs Noise", fontweight="bold")
    ax3.set_xlabel("Noise Factor")
    ax3.set_ylabel("Similarity Ratio")
    ax3.set_ylim(-0.05, 1.1)
    ax3.grid(True, alpha=0.25)

    ax4 = fig.add_subplot(grid[1, 0])
    tx_flat = np.column_stack([tx_symbols.real, tx_symbols.imag]).reshape(-1)
    rx_flat = raw_pairs.reshape(-1)
    samples = np.arange(min(60, tx_flat.size))
    ax4.plot(samples, tx_flat[samples], label="Transmitted", color="c")
    ax4.plot(samples, rx_flat[samples], "--", label=f"Raw channel output noise={mid_noise}", color="orange", alpha=0.8)
    ax4.set_title("Signal Waveform Comparison", fontweight="bold")
    ax4.set_xlabel("Sample Index")
    ax4.set_ylabel("Amplitude")
    ax4.grid(True, alpha=0.25)
    ax4.legend()

    ax5 = fig.add_subplot(grid[1, 1])
    scatter_noises = [nf for nf in noise_factors if nf > 0][:4]
    colors = plt.cm.viridis(np.linspace(0.1, 0.95, len(scatter_noises)))
    for color, nf in zip(colors, scatter_noises):
        eq_symbols = results[nf][2]
        ax5.scatter(eq_symbols.real, eq_symbols.imag, s=18, alpha=0.5, color=color, label=f"noise={nf}")
    ax5.scatter(ideal.real, ideal.imag, marker="x", s=80, c="black", linewidths=1.8, label="Ideal")
    ax5.set_title("Constellations at Different Noise Levels", fontweight="bold")
    ax5.set_xlabel("In-phase (I)")
    ax5.set_ylabel("Quadrature (Q)")
    ax5.set_xlim(-8, 8)
    ax5.set_ylim(-8, 8)
    ax5.set_aspect("equal")
    ax5.grid(True, alpha=0.25)
    ax5.legend(fontsize=8)

    ax6 = fig.add_subplot(grid[1, 2])
    bar_colors = plt.cm.coolwarm(np.linspace(0.1, 0.9, len(noise_factors)))
    bars = ax6.bar([str(nf) for nf in noise_factors], similarities, color=bar_colors, edgecolor="k")
    ax6.set_title("Similarity by Noise Level", fontweight="bold")
    ax6.set_xlabel("Noise Factor")
    ax6.set_ylabel("Similarity Ratio")
    ax6.set_ylim(0, 1.15)
    ax6.grid(True, axis="y", alpha=0.25)
    for bar, value in zip(bars, similarities):
        ax6.text(bar.get_x() + bar.get_width() / 2, value + 0.03, f"{value:.2f}", ha="center", fontsize=9, fontweight="bold")

    save_dashboard(fig, "qam16_noise_dashboard.png")
    plt.show()


def main():
    message = "ECE Communication Engineering 16-QAM dashboard"
    noise_factors = [0.0, 0.1, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0]
    results = {}

    print("--- 16-QAM noise robustness ---")
    for noise_factor in noise_factors:
        results[noise_factor] = run_trial(message, noise_factor)
        recovered = results[noise_factor][3]
        score = results[noise_factor][4]
        preview = ascii(recovered[:35])
        print(f"noise_factor={noise_factor:.1f} similarity={score:.2f} recovered={preview}")

    draw_dashboard(message, noise_factors, results)


if __name__ == "__main__":
    main()
