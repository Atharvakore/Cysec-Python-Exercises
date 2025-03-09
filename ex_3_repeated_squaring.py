
def fast_power(base: int, exponent: int, modulus: int) -> int:
    if modulus == 1:
        return 0
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        return fast_power(base**2 % modulus, exponent // 2, modulus)
    else:
        return (base * fast_power(base**2 % modulus, (exponent - 1) // 2, modulus)) % modulus

def main() -> None:
    assert fast_power(3, 16, 49) == 25
    assert fast_power(586561983649063, 982471150907619, 700106762604573) == 482959092846448


if __name__ == "__main__":
    main()
