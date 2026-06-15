import heapq
from itertools import count


def huffman_codes(probabilities):
    tie_breaker = count()
    heap = [(prob, next(tie_breaker), symbol) for symbol, prob in probabilities.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        p1, _, left = heapq.heappop(heap)
        p2, _, right = heapq.heappop(heap)
        heapq.heappush(heap, (p1 + p2, next(tie_breaker), (left, right)))

    root = heap[0][2]
    codes = {}

    def walk(node, prefix):
        if isinstance(node, tuple):
            walk(node[0], prefix + "0")
            walk(node[1], prefix + "1")
        else:
            codes[node] = prefix or "0"

    walk(root, "")
    return codes


def main():
    probabilities = {"A": 0.4, "B": 0.2, "C": 0.2, "D": 0.1, "E": 0.1}
    codes = huffman_codes(probabilities)
    average_length = sum(probabilities[symbol] * len(code) for symbol, code in codes.items())

    print("Huffman codes:")
    for symbol in sorted(codes):
        print(f"{symbol}: {codes[symbol]}")
    print(f"Average length = {average_length:.3f} bits/symbol")


if __name__ == "__main__":
    main()
