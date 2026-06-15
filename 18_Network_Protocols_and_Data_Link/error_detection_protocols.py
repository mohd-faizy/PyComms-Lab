"""Error detection at the data-link layer.

Demonstrates parity check, Internet checksum, and CRC-based frame-level
error detection.  Reports detection vs miss rates for random bit errors.
"""

import numpy as np
import matplotlib.pyplot as plt


# ---- Parity Check ----
def add_even_parity(frame):
    """Append a parity bit for even parity."""
    return np.append(frame, np.sum(frame) % 2)


def check_even_parity(frame_with_parity):
    return np.sum(frame_with_parity) % 2 == 0


# ---- Internet Checksum (16-bit) ----
def internet_checksum(data_bytes):
    """Compute a 16-bit one's-complement checksum."""
    if len(data_bytes) % 2 != 0:
        data_bytes = np.append(data_bytes, 0)
    total = 0
    for i in range(0, len(data_bytes), 2):
        word = (int(data_bytes[i]) << 8) + int(data_bytes[i + 1])
        total += word
        total = (total & 0xFFFF) + (total >> 16)  # carry wraparound
    return (~total) & 0xFFFF


# ---- CRC ----
def crc_remainder(data, poly):
    """Compute CRC remainder using binary polynomial division."""
    d = list(data.copy())
    poly_len = len(poly)
    d.extend([0] * (poly_len - 1))
    for i in range(len(data)):
        if d[i] == 1:
            for j in range(poly_len):
                d[i + j] ^= poly[j]
    return np.array(d[-(poly_len - 1):], dtype=int)


def main():
    rng = np.random.default_rng(42)
    n_trials = 1000
    frame_len = 32

    # CRC-8 polynomial: x^8 + x^2 + x + 1 -> [1,0,0,0,0,0,1,1,1]
    crc_poly = np.array([1, 0, 0, 0, 0, 0, 1, 1, 1], dtype=int)

    ber_values = np.arange(0.001, 0.15, 0.005)
    parity_miss = []
    checksum_miss = []
    crc_miss = []

    for ber in ber_values:
        p_miss, cs_miss, c_miss = 0, 0, 0
        for _ in range(n_trials):
            frame = rng.integers(0, 2, frame_len)

            # --- Parity ---
            parity_frame = add_even_parity(frame)
            # Introduce errors
            errors = rng.random(len(parity_frame)) < ber
            rx_parity = parity_frame ^ errors.astype(int)
            if errors.any() and check_even_parity(rx_parity):
                p_miss += 1

            # --- Internet checksum ---
            chksum = internet_checksum(frame)
            rx_frame = frame ^ (rng.random(frame_len) < ber).astype(int)
            rx_chksum = internet_checksum(rx_frame)
            if not np.array_equal(frame, rx_frame) and rx_chksum == chksum:
                cs_miss += 1

            # --- CRC ---
            crc = crc_remainder(frame, crc_poly)
            tx_crc = np.append(frame, crc)
            errors_crc = (rng.random(len(tx_crc)) < ber).astype(int)
            rx_crc_frame = tx_crc ^ errors_crc
            rx_remainder = crc_remainder(rx_crc_frame[:frame_len], crc_poly)
            if errors_crc.any() and np.array_equal(rx_remainder,
                                                    rx_crc_frame[frame_len:]):
                c_miss += 1

        parity_miss.append(p_miss / n_trials)
        checksum_miss.append(cs_miss / n_trials)
        crc_miss.append(c_miss / n_trials)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(ber_values * 100, parity_miss, "o-", label="Even Parity",
            markersize=4)
    ax.plot(ber_values * 100, checksum_miss, "s-", label="Internet Checksum",
            markersize=4)
    ax.plot(ber_values * 100, crc_miss, "^-", label="CRC-8", markersize=4)
    ax.set_title("Undetected Error Rate by Detection Method", fontsize=13)
    ax.set_xlabel("Bit Error Rate (%)")
    ax.set_ylabel("Fraction of Errors Missed")
    ax.legend()
    ax.grid(True)
    fig.tight_layout()
    plt.show()

    print("CRC provides the strongest error detection among the three methods.")
    print("Parity check can only detect odd numbers of bit errors.")


if __name__ == "__main__":
    main()
