import math


def orbital_period(semi_major_axis_m):
    gravitational_parameter = 3.986004418e14
    return 2 * math.pi * math.sqrt(semi_major_axis_m**3 / gravitational_parameter)


def main():
    earth_radius_m = 6371e3
    orbit_altitudes_km = {
        "LEO": 500,
        "MEO": 20_200,
        "GEO": 35_786,
    }

    for orbit, altitude_km in orbit_altitudes_km.items():
        radius = earth_radius_m + altitude_km * 1000
        period_seconds = orbital_period(radius)
        velocity = 2 * math.pi * radius / period_seconds
        print(f"{orbit}:")
        print(f"  Altitude: {altitude_km:,.0f} km")
        print(f"  Period: {period_seconds / 60:.2f} minutes")
        print(f"  Orbital velocity: {velocity / 1000:.2f} km/s")


if __name__ == "__main__":
    main()
