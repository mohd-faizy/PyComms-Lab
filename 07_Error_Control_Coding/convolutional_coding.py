import numpy as np


def parity(bits):
    return int(np.sum(bits) % 2)


def convolutional_encode(bits):
    state = [0, 0]
    encoded = []

    for bit in bits:
        register = [bit] + state
        encoded.extend([parity(register), parity([register[0], register[2]])])
        state = [bit, state[0]]

    return np.array(encoded, dtype=int)


def main():
    bits = np.array([1, 0, 1, 1, 0, 0, 1], dtype=int)
    encoded = convolutional_encode(bits)
    print("Input bits:  ", "".join(map(str, bits)))
    print("Encoded bits:", "".join(map(str, encoded)))


if __name__ == "__main__":
    main()
