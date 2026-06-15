import numpy as np


def main():
    walsh = np.array(
        [
            [1, 1, 1, 1],
            [1, -1, 1, -1],
            [1, 1, -1, -1],
            [1, -1, -1, 1],
        ]
    )

    user1_bits = np.array([1, 0, 1, 1])
    user2_bits = np.array([0, 1, 1, 0])
    user1_symbols = 2 * user1_bits - 1
    user2_symbols = 2 * user2_bits - 1

    spread1 = np.kron(user1_symbols, walsh[1])
    spread2 = np.kron(user2_symbols, walsh[2])
    channel = spread1 + spread2

    recovered1 = []
    recovered2 = []
    for i in range(user1_bits.size):
        chips = channel[i * 4 : (i + 1) * 4]
        recovered1.append(int(np.dot(chips, walsh[1]) > 0))
        recovered2.append(int(np.dot(chips, walsh[2]) > 0))

    print("User 1 bits:      ", user1_bits)
    print("Recovered user 1: ", np.array(recovered1))
    print("User 2 bits:      ", user2_bits)
    print("Recovered user 2: ", np.array(recovered2))


if __name__ == "__main__":
    main()
