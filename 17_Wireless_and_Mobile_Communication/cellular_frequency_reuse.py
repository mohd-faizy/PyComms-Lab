import numpy as np
import matplotlib.pyplot as plt


def hexagon(center_x, center_y, radius):
    angles = np.linspace(0, 2 * np.pi, 7) + np.pi / 6
    return center_x + radius * np.cos(angles), center_y + radius * np.sin(angles)


def main():
    reuse_factor = 7
    radius = 1.0
    colors = ["C0", "C1", "C2", "C3", "C4", "C5", "C6"]
    cells = []

    for q in range(-2, 3):
        for r in range(-2, 3):
            x = radius * np.sqrt(3) * (q + r / 2)
            y = radius * 1.5 * r
            cluster_id = (q + 2 * r) % reuse_factor
            cells.append((x, y, cluster_id))

    plt.figure(figsize=(8, 7))
    for x, y, cluster_id in cells:
        hx, hy = hexagon(x, y, radius)
        plt.fill(hx, hy, alpha=0.35, color=colors[cluster_id])
        plt.plot(hx, hy, color="black", linewidth=0.8)
        plt.text(x, y, str(cluster_id + 1), ha="center", va="center", weight="bold")

    plt.title("Cellular Frequency Reuse Pattern, N = 7")
    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
