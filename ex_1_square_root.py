def square_root(n):
    return round(n ** 0.5, 2)


def main() -> None:
    assert square_root(3) == 1.73
    assert square_root(16) == 4.0
    assert square_root(1337) == 36.57


if __name__ == '__main__':
    main()
