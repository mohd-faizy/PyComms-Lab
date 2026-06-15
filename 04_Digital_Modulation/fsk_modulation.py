import numpy as np
import matplotlib.pyplot as plt


def main():
    bits = np.array([1, 0, 1, 1, 0, 1, 0, 0])
    bit_rate = 50
    samples_per_bit = 200
    fs = bit_rate * samples_per_bit
    f0 = 600
    f1 = 1400

    bit_stream = np.repeat(bits, samples_per_bit)
    t = np.arange(bit_stream.size) / fs
    frequencies = np.where(bit_stream == 1, f1, f0)
    phase = 2 * np.pi * np.cumsum(frequencies) / fs
    fsk = np.cos(phase)

    fig, axes = plt.subplots(2, 1, figsize=(10, 5), sharex=True)
    axes[0].step(t, bit_stream, where="post")
    axes[0].set_title("Binary Data")
    axes[1].plot(t, fsk)
    axes[1].set_title("Binary FSK Signal")

    for ax in axes:
        ax.grid(True)
    axes[-1].set_xlabel("Time (s)")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
