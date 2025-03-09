def calculate_modulo(a, n):
    return f"{a} modulo {n} is {a % n}"


def main() -> None:
    assert calculate_modulo(6, 2) == "6 modulo 2 is 0"
    assert calculate_modulo(1337, 42) == "1337 modulo 42 is 35"
    assert calculate_modulo(-25, 4) == "-25 modulo 4 is 3"


if __name__ == "__main__":
    main()
