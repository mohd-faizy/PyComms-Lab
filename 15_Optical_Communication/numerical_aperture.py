import math


def main():
    core_index = 1.48
    cladding_index = 1.46
    outside_index = 1.0

    numerical_aperture = math.sqrt(core_index**2 - cladding_index**2)
    acceptance_angle = math.degrees(math.asin(numerical_aperture / outside_index))
    relative_index_difference = (core_index - cladding_index) / core_index

    print(f"Core refractive index: {core_index}")
    print(f"Cladding refractive index: {cladding_index}")
    print(f"Numerical aperture: {numerical_aperture:.3f}")
    print(f"Acceptance angle: {acceptance_angle:.2f} degrees")
    print(f"Relative index difference: {relative_index_difference * 100:.2f}%")


if __name__ == "__main__":
    main()
