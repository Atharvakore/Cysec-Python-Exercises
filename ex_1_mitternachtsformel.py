def mitternachtsformel(a, b, c):
    return round(max((-b + (b * b - 4 * a * c) ** 0.5) / (2 * a), (-b - (b * b - 4 * a * c) ** 0.5) / (2 * a)), 2)


def main() -> None:
    assert mitternachtsformel(2, 8, 2) == -0.27
    assert mitternachtsformel(-7, 7, 3) == 1.32


if __name__ == '__main__':
    main()
