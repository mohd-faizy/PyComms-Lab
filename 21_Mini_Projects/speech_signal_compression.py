import numpy as np
import matplotlib.pyplot as plt


def mu_law_compress(x, mu=255):
    return np.sign(x) * np.log1p(mu * np.abs(x)) / np.log1p(mu)


def mu_law_expand(y, mu=255):
    return np.sign(y) * (1 / mu) * ((1 + mu) ** np.abs(y) - 1)


def main():
    fs = 8000
    t = np.arange(0, 0.04, 1 / fs)
    speech_like = (
        0.55 * np.sin(2 * np.pi * 180 * t)
        + 0.25 * np.sin(2 * np.pi * 620 * t)
        + 0.12 * np.sin(2 * np.pi * 1200 * t)
    )
    compressed = mu_law_compress(speech_like)
    quantized = np.round((compressed + 1) * 127.5).astype(np.uint8)
    restored_compressed = quantized.astype(float) / 127.5 - 1
    reconstructed = mu_law_expand(restored_compressed)
    mse = np.mean((speech_like - reconstructed) ** 2)

    print(f"8-bit mu-law reconstruction MSE: {mse:.6f}")

    plt.figure(figsize=(10, 5))
    plt.plot(t, speech_like, label="Original")
    plt.plot(t, reconstructed, "--", label="Reconstructed")
    plt.title("Speech-like Signal Compression using 8-bit mu-law PCM")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
