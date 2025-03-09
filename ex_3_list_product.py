def list_product(lst: list) -> int:
    if lst == []:
        return 0
    res = 1
    for i in lst:
        res *= i
    return res


def main() -> None:
    assert list_product([1, 4, 7, 2]) == 56
    assert list_product([3, -8, -9, 12]) == 2592
    assert list_product([]) == 0

if __name__ == '__main__':
    main()
