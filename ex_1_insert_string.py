def insert_string(original, loc, ins):
    return original[:loc] + ins + original[loc:]


def main() -> None:
    assert insert_string("Hello rld!", 6, "Wo") == "Hello World!"
    assert insert_string("", 0, "Test") == "Test"
    assert insert_string("Cy", 2, "Sec") == "CySec"


if __name__ == '__main__':
    main()
