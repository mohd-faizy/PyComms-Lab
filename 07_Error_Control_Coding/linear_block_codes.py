import numpy as np


def main():
    generator = np.array(
        [
            [1, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 1],
        ],
        dtype=int,
    )
    parity_check = np.array(
        [
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 0, 1],
        ],
        dtype=int,
    )

    message = np.array([1, 0, 1, 1], dtype=int)
    codeword = message @ generator % 2
    received = codeword.copy()
    received[2] ^= 1
    syndrome = parity_check @ received % 2

    print("Message:  ", message)
    print("Codeword: ", codeword)
    print("Received: ", received)
    print("Syndrome: ", syndrome)


if __name__ == "__main__":
    main()
