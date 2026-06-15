import numpy as np
import matplotlib.pyplot as plt


def quantize(x, bits):
    levels = 2**bits
    x_min, x_max = -1.0, 1.0
    indices = np.round((x - x_min) / (x_max - x_min) * (levels - 1)).astype(int)
    indices = np.clip(indices, 0, levels - 1)
    quantized = x_min + indices / (levels - 1) * (x_max - x_min)
    codes = [format(index, f"0{bits}b") for index in indices]
    return indices, quantized, codes


def main():
    bits_per_sample = 3
    fs = 1000
    t = np.arange(0, 0.03, 1 / fs)
    x = 0.9 * np.sin(2 * np.pi * 100 * t)
    indices, quantized, codes = quantize(x, bits_per_sample)

    for i in range(8):
        print(f"sample {i:02d}: {x[i]: .3f} -> level {indices[i]} -> bits {codes[i]}")

    plt.figure(figsize=(10, 5))
    plt.plot(t, x, label="Original")
    plt.step(t, quantized, where="mid", label=f"{bits_per_sample}-bit PCM quantized")
    plt.title("PCM Quantization and Reconstruction")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
