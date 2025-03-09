def upper_case_and_replace_vowels(my_string: str) -> str:
    return my_string.upper().replace("A", "x").replace("E", "x").replace("I", "x").replace("O", "x").replace("U", "x")


def main() -> None:
    # Tests for upper_case_and_replace_vowels function
    assert upper_case_and_replace_vowels("hello world") == "HxLLx WxRLD"
    assert upper_case_and_replace_vowels("aEu") == "xxx"


if __name__ == '__main__':
    main()
