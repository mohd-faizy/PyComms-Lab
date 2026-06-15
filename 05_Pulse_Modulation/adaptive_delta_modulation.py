import numpy as np
import matplotlib.pyplot as plt


def adaptive_delta_modulate(x, initial_step=0.04, min_step=0.01, max_step=0.2):
    reconstructed = np.zeros_like(x)
    steps = np.zeros_like(x)
    bits = np.zeros(x.size, dtype=int)
    estimate = 0.0
    step = initial_step
    previous_bit = 1

    for i, sample in enumerate(x):
        bit = 1 if sample >= estimate else 0
        if bit == previous_bit:
            step = min(max_step, step * 1.25)
        else:
            step = max(min_step, step * 0.75)

        estimate += step if bit else -step
        bits[i] = bit
        reconstructed[i] = estimate
        steps[i] = step
        previous_bit = bit

    return bits, reconstructed, steps


def main():
    t = np.linspace(0, 0.08, 400)
    x = 0.8 * np.sin(2 * np.pi * 45 * t) + 0.15 * np.sin(2 * np.pi * 180 * t)
    bits, reconstructed, steps = adaptive_delta_modulate(x)

    print("First 32 adaptive delta bits:", "".join(map(str, bits[:32])))

    fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    axes[0].plot(t, x, label="Original")
    axes[0].step(t, reconstructed, where="post", label="Adaptive reconstruction")
    axes[0].legend()
    axes[0].grid(True)
    axes[0].set_title("Adaptive Delta Modulation")
    axes[1].plot(t, steps)
    axes[1].set_title("Adaptive Step Size")
    axes[1].set_xlabel("Time (s)")
    axes[1].grid(True)

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
