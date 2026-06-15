import numpy as np


def encode_hamming_7_4(data_bits):
    d1, d2, d3, d4 = data_bits
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p4 = d2 ^ d3 ^ d4
    return np.array([p1, p2, d1, p4, d2, d3, d4], dtype=int)


def decode_hamming_7_4(codeword):
    c = codeword.copy()
    s1 = c[0] ^ c[2] ^ c[4] ^ c[6]
    s2 = c[1] ^ c[2] ^ c[5] ^ c[6]
    s4 = c[3] ^ c[4] ^ c[5] ^ c[6]
    error_position = s1 + 2 * s2 + 4 * s4

    if error_position:
        c[error_position - 1] ^= 1

    data = c[[2, 4, 5, 6]]
    return data, error_position, c


def main():
    data = np.array([1, 0, 1, 1], dtype=int)
    codeword = encode_hamming_7_4(data)
    received = codeword.copy()
    received[4] ^= 1
    decoded, error_position, corrected = decode_hamming_7_4(received)

    print("Data:     ", data)
    print("Codeword: ", codeword)
    print("Received: ", received)
    print(f"Error at position: {error_position}")
    print("Corrected:", corrected)
    print("Decoded:  ", decoded)


if __name__ == "__main__":
    main()
