"""Bose-Chaudhuri-Hocquenghem (BCH) Cyclic Code.

Simulates the binary BCH (15, 7) error correcting code, demonstrating systematic
encoding via polynomial division and evaluating Bit Error Rate (BER) performance
to show coding gain over an AWGN channel with BPSK modulation.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# BCH (15, 7) Generator Polynomial: g(x) = x^8 + x^7 + x^6 + x^4 + x + 1
# Represented as binary array: MSB is x^8, LSB is x^0
G_POLY = np.array([1, 1, 1, 0, 1, 0, 0, 0, 1])
N = 15
K = 7
N_K = N - K  # 8 parity bits


def bch_encode(msg_bits):
    """Systematically encode a block of K=7 bits into N=15 bits.

    codeword = msg_bits * x^(N_K) + Remainder(msg_bits * x^(N_K) / g(x))
    """
    codeword = np.zeros(N, dtype=int)
    codeword[:K] = msg_bits
    
    # Polynomial division over GF(2)
    rem = np.copy(codeword)
    for i in range(K):
        if rem[i] == 1:
            rem[i : i + len(G_POLY)] ^= G_POLY
            
    # Remainder is in the last N_K positions
    codeword[K:] = rem[K:]
    return codeword


def gf_add(x, y):
    return x ^ y


# GF(2^4) tables for decoding (primitive poly: x^4 + x + 1)
GF_EXP = [1, 2, 4, 8, 3, 6, 12, 11, 5, 10, 7, 14, 15, 13, 9, 1, 2, 4, 8, 3, 6, 12, 11, 5, 10, 7, 14, 15, 13, 9, 1]
GF_LOG = [0, 0, 1, 4, 2, 8, 5, 10, 3, 14, 9, 7, 6, 13, 11, 12]

def gf_mul(x, y):
    if x == 0 or y == 0:
        return 0
    return GF_EXP[GF_LOG[x] + GF_LOG[y]]


def bsc_bch_decode(received):
    """Simple BCH (15, 7) decoder correcting up to t=2 bit errors using syndromes.

    Calculates S_1 = received(alpha^1) and S_3 = received(alpha^3) over GF(2^4).
    """
    # Calculate Syndromes S_1 and S_3
    # S_j = sum_{i=0}^{N-1} received[N-1-i] * alpha^(j*i)
    s1 = 0
    s3 = 0
    for i in range(N):
        bit = received[N - 1 - i]
        if bit == 1:
            s1 ^= GF_EXP[i % 15]
            s3 ^= GF_EXP[(3 * i) % 15]

    if s1 == 0 and s3 == 0:
        return received[:K], 0  # No errors

    # If s1 is zero but s3 is not, or vice versa (odd cases), we might have > 2 errors.
    # Error locator polynomial: Lambda(x) = 1 + Lambda_1*x + Lambda_2*x^2
    # Lambda_1 = S_1
    # Lambda_2 = (S_3 + S_1^3) / S_1
    if s1 == 0:
        # Cannot divide by S_1, indicates more than 2 errors or decoding failure
        return received[:K], -1

    s1_cubed = gf_mul(gf_mul(s1, s1), s1)
    num = s1_cubed ^ s3
    lamb2 = gf_mul(num, GF_EXP[(15 - GF_LOG[s1]) % 15])  # num / s1
    lamb1 = s1

    # Chien Search to find roots of Lambda(x) = 1 + lamb1*x + lamb2*x^2
    # Check each position i (from 0 to N-1) for error
    # x = alpha^i is root?
    corrected = np.copy(received)
    err_count = 0
    err_positions = []

    for i in range(N):
        x = GF_EXP[i]
        x_sq = gf_mul(x, x)
        val = 1 ^ gf_mul(lamb1, x) ^ gf_mul(lamb2, x_sq)
        if val == 0:
            err_pos = (15 - i) % 15  # Bit index in systematic code (0-indexed)
            if err_pos < N:
                err_positions.append(err_pos)
                err_count += 1

    # Correct the identified bits
    if 0 < err_count <= 2:
        for pos in err_positions:
            corrected[N - 1 - pos] ^= 1
        return corrected[:K], err_count
    
    # Decoding failure (more than 2 errors)
    return received[:K], -1


def main():
    print("=== BCH (15, 7) Code Demonstration ===")
    msg = np.array([1, 0, 1, 1, 0, 0, 1])
    codeword = bch_encode(msg)
    print(f"Original Message:   {msg}")
    print(f"BCH Codeword:       {codeword}")

    # Inject 2 errors
    recv = np.copy(codeword)
    recv[3] ^= 1
    recv[9] ^= 1
    print(f"Received (with 2 errors): {recv}")
    
    decoded_msg, errors = bsc_bch_decode(recv)
    print(f"Decoded Message:    {decoded_msg} (Errors corrected: {errors})")
    print(f"Success:            {np.array_equal(msg, decoded_msg)}")

    # --- BER Simulation over AWGN channel ---
    ebno_db = np.arange(0, 12, 1)
    ber_uncoded = []
    ber_coded = []

    np.random.seed(42)
    num_blocks = 2000

    for ebno in ebno_db:
        # Eb/N0 relationship: Es/N0 = Eb/N0 * R_code
        r_code = K / N
        snr_linear = 10 ** (ebno / 10.0) * r_code
        noise_std = 1.0 / np.sqrt(2.0 * snr_linear)

        errors_uncoded = 0
        errors_coded = 0
        total_bits = num_blocks * K

        for _ in range(num_blocks):
            msg_bits = np.random.randint(0, 2, K)
            
            # --- Uncoded BPSK Transmission ---
            tx_uncoded = 2 * msg_bits - 1  # 0->-1, 1->1
            rx_uncoded = tx_uncoded + np.random.normal(0, noise_std, K)
            est_uncoded = (rx_uncoded > 0).astype(int)
            errors_uncoded += np.sum(msg_bits != est_uncoded)

            # --- BCH Coded BPSK Transmission ---
            cw = bch_encode(msg_bits)
            tx_coded = 2 * cw - 1
            rx_coded = tx_coded + np.random.normal(0, noise_std, N)
            est_coded_bits = (rx_coded > 0).astype(int)
            
            dec_msg, _ = bsc_bch_decode(est_coded_bits)
            errors_coded += np.sum(msg_bits != dec_msg)

        ber_uncoded.append(errors_uncoded / total_bits)
        ber_coded.append(errors_coded / total_bits)

    # Theoretical uncoded BPSK BER
    ebno_lin = 10 ** (ebno_db / 10.0)
    ber_theory = 0.5 * scipy_erfc_approx(np.sqrt(ebno_lin))

    plt.figure(figsize=(9, 6))
    plt.semilogy(ebno_db, ber_theory, "k--", label="Theoretical Uncoded BPSK")
    plt.semilogy(ebno_db, ber_uncoded, "o", label="Simulated Uncoded BPSK", color="gray")
    plt.semilogy(ebno_db, ber_coded, "s-", label="Simulated BCH(15,7) Coded BPSK", color="c", linewidth=2)
    plt.title("BCH (15, 7) Code Performance over AWGN Channel", fontsize=13, fontweight="bold")
    plt.xlabel("Eb/N0 (dB)")
    plt.ylabel("Bit Error Rate (BER)")
    plt.ylim(1e-5, 0.5)
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()


def scipy_erfc_approx(x):
    """Approximation of complementary error function erfc(x) for simplicity."""
    from scipy.special import erfc
    return erfc(x)


if __name__ == "__main__":
    main()
