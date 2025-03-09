def egg_classifier(weight: int, is_white: bool, living_conditions: str) -> str:
    if weight <= 0:
        return "Error"
    elif weight < 53:
        size = "S"
    elif weight < 63:
        size = "M"
    elif weight < 73:
        size = "L"
    else:
        size = "XL"
    if is_white:
        color = "white"
    else:
        color = "brown"
    return f"Size: {size}; Color: {color}; Living Conditions: {living_conditions}"


def main() -> None:
    # Tests only for student side debugging
    assert egg_classifier(-154, True, "Freiland") == "Error"
    assert egg_classifier(62, False, "Bio") == "Size: M; Color: brown; Living Conditions: Bio"
    assert egg_classifier(124, True, "Kaefig") == "Size: XL; Color: white; Living Conditions: Kaefig"


if __name__ == '__main__':
    main()
