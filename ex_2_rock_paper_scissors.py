def rock_paper_scissors(symbol_1: str, symbol_2: str) -> str:
    # player 1 wins
    valid_symbols = ["rock", "paper", "scissors", "well"]
    if symbol_1 not in valid_symbols or symbol_2 not in valid_symbols:
        return "incorrect input"
    if symbol_1 == symbol_2:
        return "tie"
    if symbol_1 == "paper" and (symbol_2 == "rock" or symbol_2 == "well"):
        return "player_1"
    if symbol_1 == "rock" and symbol_2 == "scissors":
        return "player_1"
    if symbol_1 == "scissors" and symbol_2 == "paper":
        return "player_1"
    if symbol_1 == "well" and (symbol_2 == "rock" or symbol_2 == "scissors"):
        return "player_1"
    # player 2 wins
    if symbol_2 == "paper" and (symbol_1 == "rock" or symbol_1 == "well"):
        return "player_2"
    if symbol_2 == "rock" and symbol_1 == "scissors":
        return "player_2"
    if symbol_2 == "scissors" and symbol_1 == "paper":
        return "player_2"
    if symbol_2 == "well" and (symbol_1 == "rock" or symbol_1 == "scissors"):
        return "player_2"


def main() -> None:
    # Tests only for student side debugging
    assert rock_paper_scissors("rock", "scissors") == "player_1"
    assert rock_paper_scissors("well", "paper") == "player_2"
    assert rock_paper_scissors("well", "stone") == "incorrect input"


if __name__ == '__main__':
    main()
