"""One shot Wordle loops"""

__author__ = "730397634"

correct: str = "python"
guess = input("What is your 6-letter guess? ")

if guess == correct:
    print("Woo! You got it! ")
elif len(guess) == len(correct):
    print("Not quite. Play again soon! ")
while len(guess) != len(correct):
    print("That was not 6 letters! Try again:")
    guess = input("What is your 6-letter guess? ")
    if guess == correct:
        print("Woo! You got it! ")
    elif len(guess) == len(correct):
        print("Not quite. Play again soon! ")
    
first_index = 0
emoji = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while first_index < len(correct):
    if guess[first_index] == correct[first_index]:
        emoji = emoji + GREEN_BOX
    else:
        anywhere = False
        index_checker = 0
        while anywhere is False and index_checker < len(correct):
            if correct[index_checker] == guess[first_index]:
                anywhere = True
            else:
                index_checker = index_checker + 1 
        if anywhere is True:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    first_index = first_index + 1
print(emoji)