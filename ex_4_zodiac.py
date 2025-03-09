
def zodiac(birth_year: int) -> str:
    signs = {
        1924 % 12: "Rat",
        1925 % 12: "Ox",
        1926 % 12: "Tiger",
        1927 % 12: "Rabbit",
        1928 % 12: "Dragon",
        1929 % 12: "Snake",
        1930 % 12: "Horse",
        1931 % 12: "Goat",
        1932 % 12: "Monkey",
        1933 % 12: "Rooster",
        1934 % 12: "Dog",
        1935 % 12: "Pig"
    }

    return signs[birth_year % 12]


def main() -> None:
    # Tests for student side debugging only
    assert zodiac(2023) == "Rabbit"
    assert zodiac(2002) == "Horse"


if __name__ == '__main__':
    main()
