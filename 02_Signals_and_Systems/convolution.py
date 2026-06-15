import numpy as np
import matplotlib.pyplot as plt


def main():
    t = np.linspace(-2, 2, 800)
    dt = t[1] - t[0]

    x = np.where(np.abs(t) <= 0.5, 1.0, 0.0)
    h = np.exp(-3 * t) * (t >= 0)
    y = np.convolve(x, h, mode="same") * dt

    fig, axes = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
    axes[0].plot(t, x)
    axes[0].set_title("Input x(t): rectangular pulse")
    axes[1].plot(t, h)
    axes[1].set_title("Impulse response h(t): decaying exponential")
    axes[2].plot(t, y)
    axes[2].set_title("Output y(t) = x(t) * h(t)")

    for ax in axes:
        ax.grid(True)
        ax.set_ylabel("Amplitude")
    axes[-1].set_xlabel("Time (s)")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
