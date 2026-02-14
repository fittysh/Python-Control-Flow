print("I have information for the following planets:\n")
print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")


def calculate_planet_weight(earth_weight: float, planet_number: int) -> float:
    """Calculate weight on a selected planet using an if/elif chain."""
    if earth_weight <= 0:
        raise ValueError("Earth weight must be greater than 0.")

    if planet_number == 1:
        return earth_weight * 0.91  # Venus
    elif planet_number == 2:
        return earth_weight * 0.38  # Mars
    elif planet_number == 3:
        return earth_weight * 2.34  # Jupiter
    elif planet_number == 4:
        return earth_weight * 1.06  # Saturn
    elif planet_number == 5:
        return earth_weight * 0.92  # Uranus
    elif planet_number == 6:
        return earth_weight * 1.19  # Neptune
    else:
        raise ValueError("Planet number must be between 1 and 6.")


def main() -> None:
    earth_weight = 185
    planet_number = 3

    try:
        planet_weight = calculate_planet_weight(earth_weight, planet_number)
        print(f"Your weight on planet {planet_number}: {planet_weight:.2f}")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
