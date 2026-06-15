import numpy as np
import matplotlib.pyplot as plt


def delta_modulate(x, step):
    reconstructed = np.zeros_like(x)
    bits = np.zeros(x.size, dtype=int)
    estimate = 0.0

    for i, sample in enumerate(x):
        if sample >= estimate:
            bits[i] = 1
            estimate += step
        else:
            bits[i] = 0
            estimate -= step
        reconstructed[i] = estimate

    return bits, reconstructed


def main():
    t = np.linspace(0, 0.05, 300)
    x = 0.9 * np.sin(2 * np.pi * 60 * t)
    bits, reconstructed = delta_modulate(x, step=0.08)

    print("First 32 delta bits:", "".join(map(str, bits[:32])))

    plt.figure(figsize=(10, 5))
    plt.plot(t, x, label="Original")
    plt.step(t, reconstructed, where="post", label="Delta reconstruction")
    plt.title("Delta Modulation")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
