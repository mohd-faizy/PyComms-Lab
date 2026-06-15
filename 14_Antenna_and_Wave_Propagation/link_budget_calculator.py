import math


def free_space_path_loss_db(distance_km, frequency_mhz):
    return 32.44 + 20 * math.log10(distance_km) + 20 * math.log10(frequency_mhz)


def main():
    tx_power_dbm = 30
    tx_gain_dbi = 14
    rx_gain_dbi = 10
    cable_loss_db = 2
    misc_loss_db = 3
    distance_km = 5
    frequency_mhz = 2400

    fspl = free_space_path_loss_db(distance_km, frequency_mhz)
    rx_power = tx_power_dbm + tx_gain_dbi + rx_gain_dbi - cable_loss_db - misc_loss_db - fspl
    noise_floor = -100
    margin = rx_power - noise_floor

    print(f"Free-space path loss: {fspl:.2f} dB")
    print(f"Received power: {rx_power:.2f} dBm")
    print(f"Link margin above {noise_floor} dBm noise floor: {margin:.2f} dB")


if __name__ == "__main__":
    main()
