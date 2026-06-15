import numpy as np
import matplotlib.pyplot as plt


def main():
    theta = np.linspace(0, 2 * np.pi, 720)
    dipole_pattern = np.abs(np.sin(theta))
    cardioid_pattern = 0.5 * (1 + np.cos(theta))

    ax = plt.subplot(111, projection="polar")
    ax.plot(theta, dipole_pattern, label="Short dipole")
    ax.plot(theta, cardioid_pattern, label="Cardioid example")
    ax.set_title("Normalized Radiation Patterns")
    ax.legend(loc="upper right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
