def disjunction(set1: set, set2: set) -> bool:
    return set1.intersection(set2) == set()

def main() -> None:
    # Tests for student side debugging only
    assert not disjunction({1, 2, 3}, {2, 5})
    assert disjunction({"Pizza"}, {"Pineapple", "Cucumbers", "lettuce"})


if __name__ == '__main__':
    main()
