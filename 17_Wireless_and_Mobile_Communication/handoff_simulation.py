import numpy as np
import matplotlib.pyplot as plt


def received_power_dbm(position, base_station_position, tx_power_dbm=30, path_loss_exponent=3):
    distance = np.maximum(np.abs(position - base_station_position), 1)
    return tx_power_dbm - 10 * path_loss_exponent * np.log10(distance)


def main():
    x = np.linspace(0, 1000, 500)
    base_stations = [250, 750]
    p1 = received_power_dbm(x, base_stations[0])
    p2 = received_power_dbm(x, base_stations[1])
    hysteresis_db = 3

    serving = np.zeros_like(x, dtype=int)
    for i in range(1, x.size):
        current = serving[i - 1]
        candidate = 1 - current
        current_power = p1[i] if current == 0 else p2[i]
        candidate_power = p2[i] if candidate == 1 else p1[i]
        serving[i] = candidate if candidate_power > current_power + hysteresis_db else current

    handoff_indices = np.where(np.diff(serving) != 0)[0]
    print("Handoff positions (m):", np.round(x[handoff_indices], 1))

    plt.figure(figsize=(9, 5))
    plt.plot(x, p1, label="Base station 1")
    plt.plot(x, p2, label="Base station 2")
    for index in handoff_indices:
        plt.axvline(x[index], color="red", linestyle="--", label="Handoff" if index == handoff_indices[0] else None)
    plt.title("Mobile Handoff with Hysteresis")
    plt.xlabel("Mobile Position (m)")
    plt.ylabel("Received Power (dBm)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
