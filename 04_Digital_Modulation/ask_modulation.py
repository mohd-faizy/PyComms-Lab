import numpy as np
import matplotlib.pyplot as plt


def main():
    bits = np.array([1, 0, 1, 1, 0, 0, 1, 0])
    bit_rate = 100
    fc = 1000
    samples_per_bit = 100
    fs = bit_rate * samples_per_bit

    symbols = np.repeat(bits, samples_per_bit)
    t = np.arange(symbols.size) / fs
    carrier = np.cos(2 * np.pi * fc * t)
    ask = symbols * carrier

    fig, axes = plt.subplots(2, 1, figsize=(10, 5), sharex=True)
    axes[0].step(t, symbols, where="post")
    axes[0].set_title("Binary Data")
    axes[1].plot(t, ask)
    axes[1].set_title("ASK Signal")

    for ax in axes:
        ax.grid(True)
    axes[-1].set_xlabel("Time (s)")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
