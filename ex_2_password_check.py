from hashlib import md5


def crack_password(correct_hash: str, wordlist: str) -> str:
    with open(wordlist, "r") as f:
        for pwd in f.readlines():
            pwd = pwd.replace("\n", "")
            if md5(pwd.encode()).hexdigest() == correct_hash:
                return pwd
    return ""


def main() -> None:
    # Tests only for student side debugging
    assert crack_password("Hans", "asdhf2324#fq1sa") == "good"
    assert crack_password("Dieter", "securepassword!") == "Ok"
    assert crack_password("Kevin", "Kevin2002!") == "weak"
    assert crack_password("Bob", "qwertz") == "bad"


if __name__ == '__main__':
    main()
