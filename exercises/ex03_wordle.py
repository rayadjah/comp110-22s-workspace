"""An example of a structured Wordle."""

__author__ = "730397634"


def contains_char(searched_string: str, expected_string: str) -> bool:
    """Returns True if character is found at the index of correct word and False otherwise."""
    assert len(expected_string) == 1
    anyplace = False
    first_index = 0
    check_index = 0
    while anyplace is False and check_index < len(searched_string):
        if searched_string[check_index] == expected_string[first_index]:
            anyplace = True
        else:
            check_index += 1
    if anyplace is True:
        return True
    else:
        return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(searched_string: str, expected_string: str) -> str:
    """Returns Green for correct character/correct index, Yellow for correct character/wrong index and White for incorrect character."""
    assert len(searched_string) == len(expected_string)
    emoji = ""
    current_index = 0
    while current_index < len(expected_string):
        contains = contains_char(expected_string, searched_string[current_index])
        if contains is True:
            if searched_string[current_index] == expected_string[current_index]:
                emoji = emoji + GREEN_BOX
            else:
                emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
        
        current_index = current_index + 1
    
    return emoji


def input_guess(expected_length: int) -> str:
    """Making sure the guess is the right length."""
    print("Enter a " + str(expected_length) + " character word: ")
    guess = input()
    while len(guess) != expected_length:
        print("That wasn't " + str(expected_length) + " chars! Try again: ")
        guess = input()
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    correct = "codes"
    turns_spent = 1
    win_game = False

    while turns_spent <= 6 and win_game is False:
        print("=== Turn " + str(turns_spent) + "/6 ===")
        guess = input_guess(5)
        emojis = emojified(correct, guess)
        print(emojis)
        if guess == correct:
            win_game = True
        else:
            turns_spent = turns_spent + 1
    
    if win_game is True:
        print("You won in " + str(turns_spent) + "/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    
