def shannon_fano(items, prefix="", codes=None):
    if codes is None:
        codes = {}
    if len(items) == 1:
        codes[items[0][0]] = prefix or "0"
        return codes

    total = sum(prob for _, prob in items)
    running = 0
    split_index = 1
    best_error = total

    for i in range(1, len(items)):
        running += items[i - 1][1]
        error = abs(total / 2 - running)
        if error < best_error:
            best_error = error
            split_index = i

    shannon_fano(items[:split_index], prefix + "0", codes)
    shannon_fano(items[split_index:], prefix + "1", codes)
    return codes


def main():
    probabilities = {"A": 0.35, "B": 0.25, "C": 0.20, "D": 0.12, "E": 0.08}
    sorted_items = sorted(probabilities.items(), key=lambda item: item[1], reverse=True)
    codes = shannon_fano(sorted_items)

    print("Shannon-Fano codes:")
    for symbol in sorted(codes):
        print(f"{symbol}: {codes[symbol]}")


if __name__ == "__main__":
    main()
