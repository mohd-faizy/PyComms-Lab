import numpy as np


def encoder_output(bit, state):
    register = [bit, state[0], state[1]]
    return np.array([
        sum(register) % 2,
        (register[0] + register[2]) % 2,
    ], dtype=int)


def next_state(bit, state):
    return (bit, state[0])


def convolutional_encode(bits):
    state = (0, 0)
    encoded = []
    for bit in bits:
        encoded.extend(encoder_output(int(bit), state))
        state = next_state(int(bit), state)
    return np.array(encoded, dtype=int)


def viterbi_decode(received):
    states = [(0, 0), (0, 1), (1, 0), (1, 1)]
    paths = {state: (float("inf"), []) for state in states}
    paths[(0, 0)] = (0, [])

    for pair in received.reshape(-1, 2):
        new_paths = {state: (float("inf"), []) for state in states}
        for state, (metric, path) in paths.items():
            for bit in (0, 1):
                output = encoder_output(bit, state)
                candidate_state = next_state(bit, state)
                distance = int(np.sum(output != pair))
                candidate_metric = metric + distance
                if candidate_metric < new_paths[candidate_state][0]:
                    new_paths[candidate_state] = (candidate_metric, path + [bit])
        paths = new_paths

    best_state = min(paths, key=lambda state: paths[state][0])
    return np.array(paths[best_state][1], dtype=int), paths[best_state][0]


def main():
    bits = np.array([1, 0, 1, 1, 0, 1, 0], dtype=int)
    encoded = convolutional_encode(bits)
    received = encoded.copy()
    received[[3, 10]] ^= 1
    decoded, metric = viterbi_decode(received)

    print("Input bits:    ", "".join(map(str, bits)))
    print("Encoded bits:  ", "".join(map(str, encoded)))
    print("Received bits: ", "".join(map(str, received)))
    print("Decoded bits:  ", "".join(map(str, decoded)))
    print(f"Path metric: {metric}")


if __name__ == "__main__":
    main()
