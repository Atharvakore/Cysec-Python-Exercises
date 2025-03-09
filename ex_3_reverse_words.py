def reverse_words(s: str) -> str:
    return " ".join(i for i in s.split(" ")[::-1])

def main() -> None:
    assert reverse_words("World! Hello") == "Hello World!"
    assert reverse_words("This is a test") == "test a is This"
    assert reverse_words("Cysec ") == " Cysec"


if __name__ == '__main__':
    main()
