
def factorial(n: int) -> int:
    if n <= 1:
        return n
    return n * factorial(n - 1)


def compute_birthday_paradox(n: int) -> float:
    if n > 120:
        raise ValueError("n too large")
    if n < 2:
        raise ValueError("n too small")
    chance = 1 - factorial(365) / factorial(365 - n) / pow(365, n)
    return round(chance, 4)

if __name__ == '__main__':
    assert compute_birthday_paradox(23) == 0.5073
    try:
        compute_birthday_paradox(1)
        assert False  # should not reach here
    except ValueError as e:
        assert str(e) == 'n too small'
    except Exception:
        assert False

    try:
        compute_birthday_paradox(121)
        assert False  # should not reach here
    except ValueError as e:
        assert str(e) == 'n too large'
    except Exception:
        assert False
