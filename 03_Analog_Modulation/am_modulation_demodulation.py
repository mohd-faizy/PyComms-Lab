import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert


def main():
    fs = 20_000
    t = np.arange(0, 0.02, 1 / fs)
    fm = 200
    fc = 2500
    modulation_index = 0.7

    message = np.sin(2 * np.pi * fm * t)
    carrier = np.cos(2 * np.pi * fc * t)
    am = (1 + modulation_index * message) * carrier
    envelope = np.abs(hilbert(am))
    recovered = (envelope - np.mean(envelope)) / modulation_index

    fig, axes = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
    axes[0].plot(t, message)
    axes[0].set_title("Message Signal")
    axes[1].plot(t, am)
    axes[1].set_title("AM Signal")
    axes[2].plot(t, recovered)
    axes[2].set_title("Envelope Demodulated Signal")

    for ax in axes:
        ax.grid(True)
    axes[-1].set_xlabel("Time (s)")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
