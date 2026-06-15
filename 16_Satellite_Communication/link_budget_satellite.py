import math


def fspl_db(distance_km, frequency_ghz):
    return 92.45 + 20 * math.log10(distance_km) + 20 * math.log10(frequency_ghz)


def main():
    eirp_dbw = 48
    receiver_gain_dbi = 34
    distance_km = 38_000
    frequency_ghz = 12
    atmospheric_loss_db = 2.0
    pointing_loss_db = 1.0
    system_noise_temperature_k = 180
    bandwidth_hz = 36e6
    boltzmann_dbw_per_hz_k = -228.6

    path_loss = fspl_db(distance_km, frequency_ghz)
    received_carrier_dbw = (
        eirp_dbw
        + receiver_gain_dbi
        - path_loss
        - atmospheric_loss_db
        - pointing_loss_db
    )
    noise_dbw = boltzmann_dbw_per_hz_k + 10 * math.log10(system_noise_temperature_k) + 10 * math.log10(bandwidth_hz)
    carrier_to_noise_db = received_carrier_dbw - noise_dbw

    print(f"Free-space path loss: {path_loss:.2f} dB")
    print(f"Received carrier power: {received_carrier_dbw:.2f} dBW")
    print(f"Noise power: {noise_dbw:.2f} dBW")
    print(f"C/N: {carrier_to_noise_db:.2f} dB")


if __name__ == "__main__":
    main()
