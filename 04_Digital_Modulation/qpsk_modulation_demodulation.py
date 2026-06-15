import numpy as np
import matplotlib.pyplot as plt


QPSK_MAP = {
    (0, 0): (1 + 1j) / np.sqrt(2),
    (0, 1): (-1 + 1j) / np.sqrt(2),
    (1, 1): (-1 - 1j) / np.sqrt(2),
    (1, 0): (1 - 1j) / np.sqrt(2),
}


def text_to_bits(message):
    data = np.frombuffer(message.encode("utf-8"), dtype=np.uint8)
    return np.unpackbits(data)


def bits_to_text(bits):
    usable = bits[: len(bits) - (len(bits) % 8)]
    data = np.packbits(usable).tobytes()
    return data.decode("utf-8", errors="replace")


def qpsk_modulate(bits):
    padding = (-len(bits)) % 2
    if padding:
        bits = np.pad(bits, (0, padding))
    pairs = bits.reshape(-1, 2)
    symbols = np.array([QPSK_MAP[tuple(pair)] for pair in pairs])
    return symbols, padding


def qpsk_demodulate(symbols):
    ideal_symbols = np.array(list(QPSK_MAP.values()))
    ideal_bits = list(QPSK_MAP.keys())
    decoded = []

    for symbol in symbols:
        index = np.argmin(np.abs(symbol - ideal_symbols))
        decoded.extend(ideal_bits[index])

    return np.array(decoded, dtype=np.uint8)


def add_awgn(symbols, snr_db, rng):
    snr_linear = 10 ** (snr_db / 10)
    signal_power = np.mean(np.abs(symbols) ** 2)
    noise_power = signal_power / snr_linear
    noise = np.sqrt(noise_power / 2) * (
        rng.normal(size=symbols.size) + 1j * rng.normal(size=symbols.size)
    )
    return symbols + noise


def passband_waveform(symbols, samples_per_symbol=60, carrier_cycles=4):
    i_values = np.repeat(symbols.real, samples_per_symbol)
    q_values = np.repeat(symbols.imag, samples_per_symbol)
    t = np.arange(i_values.size) / samples_per_symbol
    carrier = np.cos(2 * np.pi * carrier_cycles * t)
    quadrature = np.sin(2 * np.pi * carrier_cycles * t)
    waveform = i_values * carrier - q_values * quadrature
    return t, waveform


def main():
    rng = np.random.default_rng(101)
    message = "QPSK communication lab"
    snr_db = 14

    bits = text_to_bits(message)
    tx_symbols, padding = qpsk_modulate(bits)
    rx_symbols = add_awgn(tx_symbols, snr_db, rng)
    decoded_bits = qpsk_demodulate(rx_symbols)

    if padding:
        decoded_bits = decoded_bits[:-padding]
    decoded_bits = decoded_bits[: bits.size]
    recovered = bits_to_text(decoded_bits)
    bit_error_rate = np.mean(decoded_bits != bits)

    print(f"Original message:  {message}")
    print(f"Recovered message: {recovered}")
    print(f"SNR: {snr_db} dB")
    print(f"Bit error rate: {bit_error_rate:.5f}")

    t, tx_waveform = passband_waveform(tx_symbols[:12])
    _, rx_waveform = passband_waveform(rx_symbols[:12])

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    axes[0].scatter(tx_symbols.real, tx_symbols.imag, s=28, label="Transmitted")
    axes[0].scatter(rx_symbols.real, rx_symbols.imag, s=18, alpha=0.55, label="Received")
    axes[0].set_title("QPSK Constellation")
    axes[0].set_xlabel("In-phase")
    axes[0].set_ylabel("Quadrature")
    axes[0].axis("equal")
    axes[0].grid(True)
    axes[0].legend()

    axes[1].plot(t, tx_waveform, label="Transmitted")
    axes[1].plot(t, rx_waveform, "--", alpha=0.8, label="Received")
    axes[1].set_title("Passband Waveform")
    axes[1].set_xlabel("Symbol Time")
    axes[1].set_ylabel("Amplitude")
    axes[1].grid(True)
    axes[1].legend()

    axes[2].step(np.arange(48), bits[:48], where="post", label="Original")
    axes[2].step(np.arange(48), decoded_bits[:48] + 0.05, where="post", label="Detected")
    axes[2].set_title("Bit Decisions")
    axes[2].set_xlabel("Bit Index")
    axes[2].set_ylim(-0.2, 1.3)
    axes[2].grid(True)
    axes[2].legend()

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
