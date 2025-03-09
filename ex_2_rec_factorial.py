
def factorial(n: int) -> int:
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def main() -> None:
    # Tests only for student side debugging
    assert factorial(2) == 2
    assert factorial(5) == 120


if __name__ == '__main__':
    main()
