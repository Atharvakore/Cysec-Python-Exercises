def crack_dh_exchange(p: int, g: int, A: int, B: int) -> int:
    for a in range(2, p):
        if pow(g, a, p) == A:
            return pow(B, a, p)


def main() -> None:
    # Tests for student side debugging only
    assert crack_dh_exchange(613, 560, 217, 150) == 285
    assert crack_dh_exchange(941, 101, 335, 500) == 608


if __name__ == '__main__':
    main()
