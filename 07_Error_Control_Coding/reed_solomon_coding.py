"""Reed-Solomon Error Control Coding.

Implements a self-contained Reed-Solomon (15, 11) encoder and decoder over GF(2^4)
capable of correcting up to t=2 symbol errors, illustrating Galois Field arithmetic,
syndrome calculation, and error correction.
"""

import numpy as np
import matplotlib.pyplot as plt

# GF(2^4) tables with primitive polynomial x^4 + x + 1 = 0 (19 decimal)
GF_EXP = [1, 2, 4, 8, 3, 6, 12, 11, 5, 10, 7, 14, 15, 13, 9, 1, 2, 4, 8, 3, 6, 12, 11, 5, 10, 7, 14, 15, 13, 9, 1]
GF_LOG = [0, 0, 1, 4, 2, 8, 5, 10, 3, 14, 9, 7, 6, 13, 11, 12]


def gf_add(x, y):
    """Addition in GF(2^m) is bitwise XOR."""
    return x ^ y


def gf_mul(x, y):
    """Multiplication in GF(2^4) using log/exp tables."""
    if x == 0 or y == 0:
        return 0
    return GF_EXP[GF_LOG[x] + GF_LOG[y]]


def gf_div(x, y):
    """Division in GF(2^4) using log/exp tables."""
    if y == 0:
        raise ZeroDivisionError()
    if x == 0:
        return 0
    return GF_EXP[(GF_LOG[x] - GF_LOG[y] + 15) % 15]


def gf_poly_mul(p, q):
    """Multiply two polynomials over GF(2^4)."""
    r = [0] * (len(p) + len(q) - 1)
    for j in range(len(p)):
        for i in range(len(q)):
            r[j + i] ^= gf_mul(p[j], q[i])
    return r


def gf_poly_eval(poly, x):
    """Evaluate polynomial poly(x) at x over GF(2^4) using Horner's method."""
    y = poly[0]
    for i in range(1, len(poly)):
        y = gf_add(gf_mul(y, x), poly[i])
    return y


def gf_poly_eval_lowest_first(poly, x):
    """Evaluate polynomial poly(x) at x over GF(2^4) with lowest-degree first."""
    y = 0
    x_pow = 1
    for coef in poly:
        y = gf_add(y, gf_mul(coef, x_pow))
        x_pow = gf_mul(x_pow, x)
    return y


# Reed-Solomon (15, 11) Code Parameters
N = 15
K = 11
T = 2  # Error correction capability (N - K) // 2


def get_generator_poly():
    """Generate RS generator polynomial g(x) = (x-a^1)(x-a^2)(x-a^3)(x-a^4)."""
    g = [1]
    for i in range(1, 2 * T + 1):
        g = gf_poly_mul(g, [1, GF_EXP[i]])
    return g


def rs_encode(msg, g):
    """Encode message polynomial of length K into systematic RS codeword of length N."""
    # Codeword c(x) = msg(x) * x^(n-k) + (msg(x) * x^(n-k) mod g(x))
    n_k = N - K
    out = list(msg) + [0] * n_k
    
    # Polynomial division
    for i in range(K):
        coef = out[i]
        if coef != 0:
            for j in range(1, len(g)):
                out[i + j] ^= gf_mul(g[j], coef)
                
    # Systematic codeword: original message + remainder
    return msg + out[K:]


def rs_calc_syndromes(msg):
    """Calculate 2*T syndromes for the received message."""
    # S_i = msg(alpha^i) for i = 1 to 2*T
    synd = [0] * (2 * T)
    for i in range(1, 2 * T + 1):
        synd[i - 1] = gf_poly_eval(msg, GF_EXP[i])
    return synd


def rs_correct_errors(received):
    """Decode and correct up to 2 symbol errors in systematic codeword."""
    synd = rs_calc_syndromes(received)
    if max(synd) == 0:
        return list(received), []  # No errors detected

    # Berlekamp-Massey Algorithm to find error locator polynomial Lambda(x)
    lamb = [1]
    b = [1]
    l_reg = 0
    m = 1
    
    for r in range(1, 2 * T + 1):
        # Calculate discrepancy d
        d = synd[r - 1]
        for j in range(1, len(lamb)):
            d ^= gf_mul(lamb[j], synd[r - 1 - j])
            
        if d == 0:
            m += 1
        else:
            lamb_t = list(lamb)
            # lambda(x) = lambda(x) + d * B(x) * x^m
            scale = [gf_mul(d, val) for val in b]
            # Zero pad scale to shift by x^m
            scaled_shifted = [0] * m + scale
            
            # Pad lambda to align lengths
            max_len = max(len(lamb), len(scaled_shifted))
            lamb_pad = lamb + [0] * (max_len - len(lamb))
            scaled_shifted_pad = scaled_shifted + [0] * (max_len - len(scaled_shifted))
            
            lamb = [gf_add(x_val, y_val) for x_val, y_val in zip(lamb_pad, scaled_shifted_pad)]
            
            if 2 * l_reg < r:
                l_reg = r - l_reg
                b = [gf_div(val, d) for val in lamb_t]
                m = 1
            else:
                m += 1

    # Chien Search to find error locations (roots of Lambda(x))
    # Lambda(x) roots are inverse of error locations
    error_locs = []
    for i in range(N):
        # x = alpha^(-i) = alpha^(15-i)
        eval_x = GF_EXP[(15 - i) % 15]
        if gf_poly_eval_lowest_first(lamb, eval_x) == 0:
            error_locs.append(i)

    # Forney Algorithm to calculate error values
    # Omega(x) = S(x) * Lambda(x) mod x^(2T)
    # Since T=2 is small, we can solve the error values directly from syndromes
    # S_1 = Y_1 + Y_2
    # S_2 = Y_1*X_1 + Y_2*X_2
    # If 1 error: Y_1 = S_1, error location X_1 = alpha^loc
    # If 2 errors: linear system
    corrected = list(received)
    
    if len(error_locs) == 1:
        loc = error_locs[0]
        x_val = GF_EXP[loc]
        # Y_1 = S_1 / X_1
        y_val = gf_div(synd[0], x_val)
        corrected[N - 1 - loc] ^= y_val
    elif len(error_locs) == 2:
        loc1, loc2 = error_locs[0], error_locs[1]
        x1 = GF_EXP[loc1]
        x2 = GF_EXP[loc2]
        
        # S_1 = Y_1*X1 + Y_2*X2
        # S_2 = Y_1*X1^2 + Y_2*X2^2
        # Let Z_1 = Y_1*X1, Z_2 = Y_2*X2
        # Z_1 + Z_2 = S_1
        # Z_1*X1 + Z_2*X2 = S_2
        # Z_1 = (S_2 + S_1*X2) / (X1 + X2)
        denom = gf_add(x1, x2)
        z1 = gf_div(gf_add(synd[1], gf_mul(synd[0], x2)), denom)
        z2 = gf_add(synd[0], z1)
        
        y1 = gf_div(z1, x1)
        y2 = gf_div(z2, x2)
        
        corrected[N - 1 - loc1] ^= y1
        corrected[N - 1 - loc2] ^= y2

    return corrected, error_locs


def main():
    g = get_generator_poly()
    
    # 11 4-bit message symbols
    msg = [5, 12, 3, 0, 15, 8, 1, 9, 2, 7, 10]
    codeword = rs_encode(msg, g)
    
    print("=== Reed-Solomon (15, 11) Simulation ===")
    print(f"Generator Polynomial coefficients: {g}")
    print(f"Original Message symbols (GF(2^4)):  {msg}")
    print(f"RS Encoded Codeword:                 {codeword}")

    # Inject 2 symbol errors
    received = list(codeword)
    received[2] ^= 9   # Inject error in symbol 2
    received[8] ^= 14  # Inject error in symbol 8
    
    print(f"Received Codeword (with 2 errors):   {received}")

    # Decode and correct
    corrected, err_locs = rs_correct_errors(received)
    
    print(f"Decoded Codeword:                    {corrected}")
    # Error locations returned by Chien search are index from right
    decoded_err_indices = [N - 1 - loc for loc in err_locs]
    print(f"Identified error symbol indices:     {decoded_err_indices}")
    print(f"Error correction successful:         {corrected == codeword}")

    # --- BER/SER simulation over channel ---
    # We will simulate Symbol Error Rate (SER) before and after RS coding
    ser_in = np.linspace(0.01, 0.3, 20)
    ser_out = []
    
    np.random.seed(42)
    num_runs = 1000

    for p in ser_in:
        uncorrected_packets = 0
        for _ in range(num_runs):
            c_word = rs_encode(list(np.random.randint(0, 16, K)), g)
            # Inject random errors with symbol error rate p
            recv = list(c_word)
            errs = 0
            for i in range(N):
                if np.random.rand() < p:
                    # XOR with random non-zero value
                    recv[i] ^= np.random.randint(1, 16)
                    errs += 1
            corr, _ = rs_correct_errors(recv)
            if corr != c_word:
                uncorrected_packets += 1
                
        ser_out.append(uncorrected_packets / num_runs)

    plt.figure(figsize=(9, 5.5))
    plt.semilogy(ser_in, ser_in, "--", label="Uncoded (No RS)", color="gray", linewidth=1.5)
    plt.semilogy(ser_in, ser_out, "o-", label="RS(15,11) Coded Word Error Rate", color="r", linewidth=2)
    plt.title("Reed-Solomon (15, 11) Code Performance over BSC-Symbol Channel", fontsize=13, fontweight="bold")
    plt.xlabel("Channel Symbol Error Rate (SER)")
    plt.ylabel("Word/Packet Error Rate")
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
