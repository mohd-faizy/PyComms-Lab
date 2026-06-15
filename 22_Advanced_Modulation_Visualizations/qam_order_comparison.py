import numpy as np
import matplotlib.pyplot as plt


def square_qam_constellation(order):
    side = int(np.sqrt(order))
    if side * side != order:
        raise ValueError("QAM order must be a perfect square")

    levels = np.arange(-(side - 1), side, 2)
    points = np.array([i + 1j * q for q in levels for i in levels])
    return points / np.sqrt(np.mean(np.abs(points) ** 2))


def add_awgn(symbols, snr_db, rng):
    snr_linear = 10 ** (snr_db / 10)
    noise_power = np.mean(np.abs(symbols) ** 2) / snr_linear
    noise = np.sqrt(noise_power / 2) * (
        rng.normal(size=symbols.size) + 1j * rng.normal(size=symbols.size)
    )
    return symbols + noise


def minimum_distance(points):
    distances = []
    for index, point in enumerate(points):
        others = np.delete(points, index)
        distances.append(np.min(np.abs(point - others)))
    return min(distances)


def main():
    rng = np.random.default_rng(404)
    orders = [4, 16, 64]
    snr_db = 18
    fig, axes = plt.subplots(1, len(orders), figsize=(14, 4))

    for ax, order in zip(axes, orders):
        ideal = square_qam_constellation(order)
        noisy = add_awgn(np.repeat(ideal, 80), snr_db, rng)
        min_dist = minimum_distance(ideal)

        ax.scatter(noisy.real, noisy.imag, s=8, alpha=0.3, label=f"Noisy at {snr_db} dB")
        ax.scatter(ideal.real, ideal.imag, marker="x", s=70, color="black", label="Ideal")
        ax.set_title(f"{order}-QAM\nmin distance={min_dist:.3f}")
        ax.set_xlabel("In-phase")
        ax.set_ylabel("Quadrature")
        ax.axis("equal")
        ax.grid(True)
        ax.legend(fontsize=8)

        print(f"{order}-QAM: average energy={np.mean(np.abs(ideal) ** 2):.2f}, minimum distance={min_dist:.3f}")

    fig.suptitle("QAM Order Comparison: Higher Order Means Tighter Symbol Spacing", fontweight="bold")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
