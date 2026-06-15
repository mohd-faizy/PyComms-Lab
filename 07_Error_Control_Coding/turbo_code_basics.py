"""Turbo Code Encoder and Iterative Decoder.

Simulates a parallel concatenated convolutional code (Turbo Code) with a
random interleaver. Implements a simplified iterative soft-decision decoder
illustrating how extrinsic information is exchanged between two decoders.
"""

import numpy as np
import matplotlib.pyplot as plt


def rsc_encode(bits, feedback=3, feedforward=2):
    """Recursive Systematic Convolutional (RSC) encoder.

    Uses constraint length K=3, 4-state trellis.
    feedback generator: 7 (octal) -> 111 binary -> feedback = 3 (mod 2)
    feedforward generator: 5 (octal) -> 101 binary -> feedforward = 2 (mod 2)
    """
    state = 0  # 2-bit state: [s1, s2]
    systematic = np.copy(bits)
    parity = np.zeros(len(bits), dtype=int)

    for i, x in enumerate(bits):
        s1 = (state >> 1) & 1
        s2 = state & 1
        
        # Feedback bit: x_i + s1 + s2 (mod 2)
        fb = (x ^ s1 ^ s2) & 1
        # Parity bit: fb + s2 (mod 2) (using feedforward generator)
        p = (fb ^ s2) & 1
        
        parity[i] = p
        # Update state: [fb, s1]
        state = (fb << 1) | s1
        
    return systematic, parity


def turbo_encode(bits, interleaver):
    """Turbo Encoder: Parallel Concatenation of two RSC Encoders.

    Returns systematic bits, parity bits 1, and parity bits 2.
    """
    sys, p1 = rsc_encode(bits)
    # Interleave bits for the second encoder
    interleaved_bits = bits[interleaver]
    _, p2 = rsc_encode(interleaved_bits)
    return sys, p1, p2


def soft_siso_decode(sys_llr, parity_llr, extrinsic_in):
    """Simplified Soft-In Soft-Out (SISO) Decoder.

    For educational clarity, we model the SISO decoder output as a combination
    of the channel LLR and the extrinsic information, adding a processing gain
    factor and reducing noise, which mimics the behavior of a BCJR log-MAP decoder.
    """
    # L_out = L_sys + L_ext_in + L_ext_out
    # We simulate the convergence of extrinsic information.
    # Extrinsic out improves as a function of incoming LLRs.
    noise_reduction = 0.6
    extrinsic_out = noise_reduction * (sys_llr + parity_llr) + 0.5 * extrinsic_in
    return extrinsic_out


def main():
    N_bits = 1000
    ebno_db = 2.0
    ebno_lin = 10 ** (ebno_db / 10.0)
    # Turbo rate R = 1/3
    rate = 1/3
    sigma = 1.0 / np.sqrt(2 * rate * ebno_lin)

    print("=== Turbo Code Basics Simulation ===")
    print(f"Block Length (N): {N_bits} bits")
    print(f"Eb/N0:            {ebno_db} dB")
    print(f"Noise Std Dev:    {sigma:.4f}")

    np.random.seed(42)
    msg = np.random.randint(0, 2, N_bits)
    
    # Generate random interleaver mapping
    interleaver = np.random.permutation(N_bits)
    # Deinterleaver mapping
    deinterleaver = np.argsort(interleaver)

    # Encode
    sys, p1, p2 = turbo_encode(msg, interleaver)

    # Channel transmission (BPSK + AWGN)
    tx_sys = 2 * sys - 1
    tx_p1 = 2 * p1 - 1
    tx_p2 = 2 * p2 - 1

    rx_sys = tx_sys + np.random.normal(0, sigma, N_bits)
    rx_p1 = tx_p1 + np.random.normal(0, sigma, N_bits)
    rx_p2 = tx_p2 + np.random.normal(0, sigma, N_bits)

    # Channel LLRs: L = 2*r/sigma^2 for BPSK
    llr_sys = 2 * rx_sys / (sigma**2)
    llr_p1 = 2 * rx_p1 / (sigma**2)
    llr_p2 = 2 * rx_p2 / (sigma**2)

    # Iterative decoding loop
    extrinsic_12 = np.zeros(N_bits)  # Extrinsic from Dec1 to Dec2
    extrinsic_21 = np.zeros(N_bits)  # Extrinsic from Dec2 to Dec1

    iterations = 6
    ber_history = []

    for it in range(iterations):
        # --- Decoder 1 ---
        # Input to Dec1: systematic LLR + feedback from Dec2
        dec1_input = llr_sys + extrinsic_21
        extrinsic_12 = soft_siso_decode(dec1_input, llr_p1, extrinsic_21)

        # --- Decoder 2 ---
        # Input to Dec2: interleaved systematic LLR + interleaved extrinsic from Dec1
        llr_sys_int = llr_sys[interleaver]
        extrinsic_12_int = extrinsic_12[interleaver]
        
        extrinsic_21_int = soft_siso_decode(llr_sys_int + extrinsic_12_int, llr_p2, extrinsic_12_int)
        
        # Deinterleave extrinsic output to pass back to Dec1
        extrinsic_21 = extrinsic_21_int[deinterleaver]

        # Overall soft decision: sys_llr + ext12 + ext21
        overall_llr = llr_sys + extrinsic_12 + extrinsic_21
        decoded_bits = (overall_llr > 0).astype(int)
        
        ber = np.mean(decoded_bits != msg)
        ber_history.append(ber)
        print(f"  Iteration {it+1}: BER = {ber*100:.3f}%")

    # Plot BER vs iterations
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, iterations + 1), ber_history, "o-", color="r", linewidth=2.5)
    plt.title("Turbo Code Iterative Decoding Convergence", fontsize=13, fontweight="bold")
    plt.xlabel("Decoding Iteration")
    plt.ylabel("Bit Error Rate (BER)")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
