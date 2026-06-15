import numpy as np
import matplotlib.pyplot as plt


def main():
    fs = 10_000
    t = np.arange(0, 0.05, 1 / fs)
    message = np.sin(2 * np.pi * 100 * t)
    sample_rate = 1000
    samples_per_pulse = fs // sample_rate
    pulse_train = np.zeros_like(t)
    pulse_train[::samples_per_pulse] = 1
    pam = np.repeat(message[::samples_per_pulse], samples_per_pulse)[: t.size]

    fig, axes = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
    axes[0].plot(t, message)
    axes[0].set_title("Message Signal")
    axes[1].stem(t[::samples_per_pulse], message[::samples_per_pulse], basefmt=" ")
    axes[1].set_title("Sampled Values")
    axes[2].step(t, pam, where="post")
    axes[2].set_title("Flat-top PAM")

    for ax in axes:
        ax.grid(True)
    axes[-1].set_xlabel("Time (s)")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
