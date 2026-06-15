import numpy as np
import matplotlib.pyplot as plt


BIT_TO_LEVEL = {
    (0, 0): -3,
    (0, 1): -1,
    (1, 1): 1,
    (1, 0): 3,
}
LEVEL_TO_BITS = {level: bits for bits, level in BIT_TO_LEVEL.items()}
LEVELS = np.array([-3, -1, 1, 3])
NORMALIZATION = np.sqrt(10)


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
    groups = bits.reshape(-1, 4)
    symbols = []

    for group in groups:
        i_level = BIT_TO_LEVEL[tuple(group[:2])]
        q_level = BIT_TO_LEVEL[tuple(group[2:])]
        symbols.append((i_level + 1j * q_level) / NORMALIZATION)

    return np.array(symbols), padding


def qam16_demodulate(symbols):
    decoded = []
    scaled_symbols = symbols * NORMALIZATION

    for symbol in scaled_symbols:
        i_level = LEVELS[np.argmin(np.abs(symbol.real - LEVELS))]
        q_level = LEVELS[np.argmin(np.abs(symbol.imag - LEVELS))]
        decoded.extend(LEVEL_TO_BITS[int(i_level)])
        decoded.extend(LEVEL_TO_BITS[int(q_level)])

    return np.array(decoded, dtype=np.uint8)


def add_awgn(symbols, snr_db, rng):
    snr_linear = 10 ** (snr_db / 10)
    signal_power = np.mean(np.abs(symbols) ** 2)
    noise_power = signal_power / snr_linear
    noise = np.sqrt(noise_power / 2) * (
        rng.normal(size=symbols.size) + 1j * rng.normal(size=symbols.size)
    )
    return symbols + noise


def main():
    rng = np.random.default_rng(116)
    message = "16-QAM modulation and demodulation"
    snr_db = 16

    bits = text_to_bits(message)
    tx_symbols, padding = qam16_modulate(bits)
    rx_symbols = add_awgn(tx_symbols, snr_db, rng)
    decoded_bits = qam16_demodulate(rx_symbols)

    if padding:
        decoded_bits = decoded_bits[:-padding]
    decoded_bits = decoded_bits[: bits.size]
    recovered = bits_to_text(decoded_bits)
    bit_error_rate = np.mean(decoded_bits != bits)
    symbol_error_rate = np.mean(np.any(decoded_bits.reshape(-1, 4) != bits.reshape(-1, 4), axis=1))

    print(f"Original message:  {message}")
    print(f"Recovered message: {recovered}")
    print(f"SNR: {snr_db} dB")
    print(f"Bit error rate: {bit_error_rate:.5f}")
    print(f"Symbol error rate: {symbol_error_rate:.5f}")

    ideal = np.array([(i + 1j * q) / NORMALIZATION for i in LEVELS for q in LEVELS])
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))

    axes[0].scatter(ideal.real, ideal.imag, marker="s", s=90, label="Ideal")
    axes[0].scatter(rx_symbols.real, rx_symbols.imag, s=18, alpha=0.55, label="Received")
    axes[0].set_title("16-QAM Constellation")
    axes[0].set_xlabel("In-phase")
    axes[0].set_ylabel("Quadrature")
    axes[0].axis("equal")
    axes[0].grid(True)
    axes[0].legend()

    axes[1].plot(tx_symbols.real[:60], label="Tx I")
    axes[1].plot(rx_symbols.real[:60], "--", label="Rx I")
    axes[1].set_title("In-phase Samples")
    axes[1].set_xlabel("Symbol Index")
    axes[1].grid(True)
    axes[1].legend()

    axes[2].plot(tx_symbols.imag[:60], label="Tx Q")
    axes[2].plot(rx_symbols.imag[:60], "--", label="Rx Q")
    axes[2].set_title("Quadrature Samples")
    axes[2].set_xlabel("Symbol Index")
    axes[2].grid(True)
    axes[2].legend()

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
