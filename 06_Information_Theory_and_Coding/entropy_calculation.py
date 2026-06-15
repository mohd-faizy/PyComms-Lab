import numpy as np


def entropy(probabilities):
    p = np.array(probabilities, dtype=float)
    p = p[p > 0]
    return -np.sum(p * np.log2(p))


def main():
    symbols = ["A", "B", "C", "D"]
    probabilities = [0.5, 0.25, 0.15, 0.10]
    h = entropy(probabilities)

    for symbol, prob in zip(symbols, probabilities):
        print(f"P({symbol}) = {prob:.2f}")
    print(f"Entropy = {h:.3f} bits/symbol")


if __name__ == "__main__":
    main()
