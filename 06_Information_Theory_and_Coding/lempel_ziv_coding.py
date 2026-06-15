"""Lempel-Ziv (LZ78) Compression Algorithm Demonstration.

Implements the dictionary-based LZ78 compression algorithm and visualises
compression ratio and dictionary size growth for different data profiles (random vs repetitive).
"""

import numpy as np
import matplotlib.pyplot as plt


def lz78_encode(text):
    """Encode text using the LZ78 compression algorithm.

    Returns the compressed tokens (index, character) and the dictionary.
    """
    dictionary = {"": 0}  # Empty string is at index 0
    dict_size = 1
    w = ""
    compressed = []

    for char in text:
        wc = w + char
        if wc in dictionary:
            w = wc
        else:
            # Output the index of w and the new character
            compressed.append((dictionary[w], char))
            # Add wc to dictionary
            dictionary[wc] = dict_size
            dict_size += 1
            w = ""

    # Handle the remaining string
    if w:
        # If the last phrase is in dictionary, output its index and empty char/EOF
        # We can find the last character of w and index of w[:-1]
        compressed.append((dictionary[w[:-1]], w[-1]))

    return compressed, dictionary


def lz78_decode(compressed):
    """Decode LZ78 compressed tokens back to original text."""
    dictionary = {0: ""}
    dict_size = 1
    decompressed = []

    for index, char in compressed:
        entry = dictionary[index] + char
        decompressed.append(entry)
        dictionary[dict_size] = entry
        dict_size += 1

    return "".join(decompressed)


def main():
    # Example sequence showing how LZ78 builds the dictionary
    sample_text = "ABABABAABABAB"
    compressed, dictionary = lz78_encode(sample_text)
    decoded = lz78_decode(compressed)

    print("=== LZ78 Encoding Step-by-Step ===")
    print(f"Original Text: '{sample_text}' (Length: {len(sample_text)})")
    print("\nEncoding process output tokens:")
    print(f"{'Token Index':<12} | {'Output (Index, Char)':<20} | {'Dictionary Phrase'}")
    print("-" * 55)
    phrases = {0: ""}
    for idx, (p_idx, char) in enumerate(compressed):
        phrase_str = phrases[p_idx] + char
        phrases[idx + 1] = phrase_str
        token_str = f"({p_idx}, '{char}')"
        print(f"{idx+1:<12} | {token_str:<20} | '{phrase_str}'")

    print(f"\nDecompressed Text matches original: {decoded == sample_text}")

    # --- Performance Evaluation (Random vs Repetitive) ---
    lengths = np.arange(10, 1001, 50)
    repetitive_ratios = []
    random_ratios = []
    
    np.random.seed(42)

    for l in lengths:
        # Repetitive: "ABC" repeated
        rep_text = "".join(["A", "B", "C"][i % 3] for i in range(l))
        # Random: characters A, B, C with equal probability
        rand_text = "".join(np.random.choice(["A", "B", "C"], l))

        comp_rep, _ = lz78_encode(rep_text)
        comp_rand, _ = lz78_encode(rand_text)

        # Estimate size in bits
        # In LZ78, each token has an index and a character.
        # Max index is dictionary size. Number of bits to represent index is ceil(log2(dict_size))
        # Char requires 8 bits (ascii) or log2(alphabet_size) (approx 2 bits for A, B, C)
        # We'll use 8 bits for char and ceil(log2(dict_size)) for index.
        
        bits_raw = l * 8
        
        # Repetitive compressed bits
        rep_dict_size = len(comp_rep)
        bits_rep_idx = np.sum([np.ceil(np.log2(i + 1)) for i in range(len(comp_rep))])
        bits_rep = bits_rep_idx + len(comp_rep) * 8
        
        # Random compressed bits
        rand_dict_size = len(comp_rand)
        bits_rand_idx = np.sum([np.ceil(np.log2(i + 1)) for i in range(len(comp_rand))])
        bits_rand = bits_rand_idx + len(comp_rand) * 8

        repetitive_ratios.append(bits_rep / bits_raw)
        random_ratios.append(bits_rand / bits_raw)

    # Plot performance curves
    plt.figure(figsize=(10, 6))
    plt.plot(lengths, repetitive_ratios, "o-", label="Repetitive Sequence ('ABC...')", color="gray", linewidth=2)
    plt.plot(lengths, random_ratios, "s-", label="Random Sequence (A, B, C)", color="r", linewidth=2)
    plt.axhline(1.0, color="grey", linestyle="--", alpha=0.7, label="No Compression Limit")
    plt.title("LZ78 Compression Ratio vs. Sequence Length", fontsize=13, fontweight="bold")
    plt.xlabel("Sequence Length (characters)")
    plt.ylabel("Compressed Size / Original Size")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
