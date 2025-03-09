def celsius_to_fahrenheit_ice(celsius: int) -> str:
    fahrenheit = round(celsius * 1.8 + 32, 2)
    if fahrenheit >= 212:
        state = "gas"
    elif fahrenheit > 32:
        state = "liquid"
    else:
        state = "solid"
    return f"H20 is {state} at {fahrenheit}f"


def main() -> None:
    # Tests only for student side debugging
    assert celsius_to_fahrenheit_ice(-12) == "H2O is solid at 10.4f"
    assert celsius_to_fahrenheit_ice(32) == "H2O is liquid at 89.6f"
    assert celsius_to_fahrenheit_ice(112) == "H2O is gas at 233.6f"


if __name__ == '__main__':
    main()
