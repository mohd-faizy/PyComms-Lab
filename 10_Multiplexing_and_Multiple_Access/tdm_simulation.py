import numpy as np
import matplotlib.pyplot as plt


def main():
    n = 80
    t = np.linspace(0, 1, n)
    ch1 = np.sin(2 * np.pi * 3 * t)
    ch2 = 0.7 * np.sin(2 * np.pi * 5 * t + 0.8)
    ch3 = 0.5 * np.cos(2 * np.pi * 2 * t)

    multiplexed = np.vstack([ch1, ch2, ch3]).T.reshape(-1)
    recovered = multiplexed.reshape(-1, 3).T

    fig, axes = plt.subplots(2, 1, figsize=(10, 6))
    axes[0].plot(t, ch1, label="Channel 1")
    axes[0].plot(t, ch2, label="Channel 2")
    axes[0].plot(t, ch3, label="Channel 3")
    axes[0].set_title("Original Channels")
    axes[0].legend()
    axes[0].grid(True)
    axes[1].plot(multiplexed, marker="o", markersize=3)
    axes[1].set_title("TDM Stream")
    axes[1].set_xlabel("Time Slot")
    axes[1].grid(True)

    print("Recovered channel 1 matches:", np.allclose(recovered[0], ch1))
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
