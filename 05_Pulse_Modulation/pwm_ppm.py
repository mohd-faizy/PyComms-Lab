import numpy as np
import matplotlib.pyplot as plt


def main():
    periods = 20
    samples_per_period = 100
    t = np.linspace(0, periods, periods * samples_per_period, endpoint=False)
    message = 0.5 + 0.4 * np.sin(2 * np.pi * t / periods * 3)
    pwm = np.zeros_like(t)
    ppm = np.zeros_like(t)

    for period in range(periods):
        start = period * samples_per_period
        width = int(message[start] * samples_per_period)
        pwm[start : start + width] = 1
        position = start + min(width, samples_per_period - 5)
        ppm[position : position + 5] = 1

    fig, axes = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
    axes[0].plot(t, message)
    axes[0].set_title("Normalized Message")
    axes[1].plot(t, pwm)
    axes[1].set_title("PWM")
    axes[2].plot(t, ppm)
    axes[2].set_title("PPM")

    for ax in axes:
        ax.grid(True)
        ax.set_ylim(-0.1, 1.1)
    axes[-1].set_xlabel("Symbol Period")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
