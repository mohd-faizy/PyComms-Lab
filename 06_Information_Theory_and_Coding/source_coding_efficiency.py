import math


def entropy(probabilities):
    return -sum(p * math.log2(p) for p in probabilities if p > 0)


def main():
    probabilities = {"A": 0.4, "B": 0.3, "C": 0.2, "D": 0.1}
    code = {"A": "0", "B": "10", "C": "110", "D": "111"}

    h = entropy(probabilities.values())
    average_length = sum(probabilities[symbol] * len(codeword) for symbol, codeword in code.items())
    efficiency = h / average_length

    print(f"Entropy = {h:.3f} bits/symbol")
    print(f"Average code length = {average_length:.3f} bits/symbol")
    print(f"Source coding efficiency = {efficiency * 100:.2f}%")


if __name__ == "__main__":
    main()
