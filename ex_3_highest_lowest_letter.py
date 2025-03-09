def highest_lowest_letter(s: str) -> tuple[int, int]:
    highest, lowest = 0, 0xff
    for c in s:
        if ord(c) > highest:
            highest = ord(c)
        if ord(c) < lowest:
            lowest = ord(c)
    return highest, lowest

def main() -> None:
    assert highest_lowest_letter("Hello World!") == (114, 32)
    assert highest_lowest_letter("AAA") == (65, 65)
    assert highest_lowest_letter(
        "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et "
        "dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet "
        "clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, "
        "consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, "
        "sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, "
        "no sea takimata sanctus est Lorem ipsum dolor sit amet.") == (121, 32)


if __name__ == '__main__':
    main()
