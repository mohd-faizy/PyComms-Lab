import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def main():
    fs = 1000
    t = np.linspace(-1, 1, 2 * fs, endpoint=False)

    signals = {
        "Sine wave": np.sin(2 * np.pi * 5 * t),
        "Square wave": signal.square(2 * np.pi * 5 * t),
        "Sawtooth wave": signal.sawtooth(2 * np.pi * 5 * t),
        "Unit step": (t >= 0).astype(float),
        "Unit impulse": np.where(np.isclose(t, 0), 1.0, 0.0),
    }

    fig, axes = plt.subplots(len(signals), 1, figsize=(10, 8), sharex=True)
    for ax, (title, values) in zip(axes, signals.items()):
        ax.plot(t, values)
        ax.set_title(title)
        ax.grid(True)

    axes[-1].set_xlabel("Time (s)")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
