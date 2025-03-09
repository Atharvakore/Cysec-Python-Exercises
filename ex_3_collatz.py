
def collatzSteps(n: int) -> int:
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (n * 3) + 1
        steps += 1
    return steps


def main() -> None:
    assert (collatzSteps(1) == 0)
    assert (collatzSteps(3) == 7)
    assert (collatzSteps(97) == 118)


if __name__ == "__main__":
    main()
