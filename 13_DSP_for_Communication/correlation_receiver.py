import numpy as np
import matplotlib.pyplot as plt


def main():
    rng = np.random.default_rng(43)
    samples_per_symbol = 80
    t = np.linspace(0, 1, samples_per_symbol, endpoint=False)
    basis0 = np.cos(2 * np.pi * 5 * t)
    basis1 = np.sin(2 * np.pi * 5 * t)
    bit = 1
    transmitted = basis1 if bit else basis0
    received = transmitted + 0.6 * rng.normal(size=samples_per_symbol)
    corr0 = np.dot(received, basis0)
    corr1 = np.dot(received, basis1)
    detected = int(corr1 > corr0)

    print(f"Correlation with basis 0: {corr0:.2f}")
    print(f"Correlation with basis 1: {corr1:.2f}")
    print(f"Detected bit: {detected}")

    plt.figure(figsize=(9, 4))
    plt.plot(t, received, label="Received")
    plt.plot(t, basis0, "--", label="Basis 0")
    plt.plot(t, basis1, "--", label="Basis 1")
    plt.title("Correlation Receiver")
    plt.xlabel("Normalized Time")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
