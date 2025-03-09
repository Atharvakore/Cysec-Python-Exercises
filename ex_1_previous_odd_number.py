# Write a Python function named previous_odd_number takes a number n and returns the previous odd number before n.
# You should not use if-elif-else constructs.

def previous_odd_number(n):
    return n - (1 + (n % 2))


def main() -> None:
    assert previous_odd_number(6) == 5
    assert previous_odd_number(81) == 79
    assert previous_odd_number(-41) == -43


if __name__ == '__main__':
    main()
