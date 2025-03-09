import string


def replacement_cipher(key_dict: dict[str, str], cipher_text: str) -> str:
    plain_text = ""
    for letter in cipher_text:
        if letter in string.ascii_letters:
            plain_text += key_dict[letter]
        else:
            plain_text += letter
    return plain_text


def main() -> None:
    # Tests for student side debugging only
    assert replacement_cipher({"e": "c", "g": "a", "d": "f", "v": "e", "r": "b"}, "egdv rgrv") == "cafe babe"


if __name__ == '__main__':
    main()
