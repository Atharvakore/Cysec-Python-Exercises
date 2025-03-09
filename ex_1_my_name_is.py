def my_name_is(name, age, height):
    return f"My name is {name}, I am {age} years old and {height}cm tall."
    pass


def main() -> None:
    assert my_name_is("Bob", 19, 170) == "My name is Bob, I am 19 years old and 170cm tall."
    assert my_name_is("Alice", 18, 165) == "My name is Alice, I am 18 years old and 165cm tall."


if __name__ == '__main__':
    main()
