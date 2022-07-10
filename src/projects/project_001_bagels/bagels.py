import platform
import random

# Settings

DIGITS: list[str] = list("0123456789")
NUM_DIGITS: int = 3
NUM_GUESSES: int = 10


def get_secret_number(notify: bool = False) -> str:
    """Return the secret number to be guessed by the user."""
    # Shuffle the list of digits
    random.shuffle(DIGITS)
    if notify:
        print("\nOK, I have another secret number in my mind. Let's play.\n")
    return "".join(DIGITS[:NUM_DIGITS])


def game(show_instructions: bool = True) -> bool:
    """Run the game and return the bool indicating whether the user wins."""
    if show_instructions:
        print(
            """
Welcome to the Bagels game!
-------------------------------------------------------------------------------
Hi! I am your Python interpreter. They call me {}.

Let's play a game...

I will think of a number composed at most of {} digits.
Note that my number includes leading zeros, but you don't have to include them.

The rules are simple. You have {} attempts to guess this number...

As soon as you provide a guess, I will respond with some clues. When I say:
- 'Pico', there is a correct digit in your guess but in the wrong position;
- 'Fermi', there is a correct digit in your guess and in the correct position;
- 'Bagels', there is no correct digits in your guess.

Keep in mind that I can say 'Pico' and 'Fermi' more than once and the order
of the clues does not matter!

Be aware I will validate your every guess: I will treat empty guesses as 0 and
ignore those composed of more than {} digits or containing other characters.

Good luck!
-------------------------------------------------------------------------------
            """.format(
                platform.python_version(),
                NUM_DIGITS,
                NUM_GUESSES,
                NUM_DIGITS,
            ),
            end="",
        )

    # Generate the secret number to be guessed
    secret_number = get_secret_number()

    # Initialize the guess counter
    guess_number: int = 1

    # Guessing flag
    guessed: bool = False

    while guess_number <= NUM_GUESSES:
        # Request a guess
        guess = input(f"Your guess no. {guess_number} is:\n> ")

        # Validate the raw guess
        if len(guess) > NUM_DIGITS or any(d not in DIGITS for d in guess):
            print("Invalid value for this guess. Sorry, you missed a try.")

        # Add leading zeros
        if len(guess) < NUM_DIGITS:
            guess = "0" * (NUM_DIGITS - len(guess)) + guess

        # Check if the secret number is guessed - if so, exit the loop
        guessed = guess == secret_number
        if guessed:
            print(
                """
-------------------------------------------------------------------------------
Yeah, you got it! Congratulations!
-------------------------------------------------------------------------------
                """
            )

            # Exit the game
            break

        # Get the clues
        clues = []
        for index in range(NUM_DIGITS):
            if guess[index] == secret_number[index]:
                clues.append("Fermi!")
            elif guess[index] in secret_number:
                clues.append("Pico!")

        if not clues:
            clues = ["Bagels!"]
        else:
            # Sort the clues to that the user is not able to deduce
            # which one is associated with given guess digit
            clues.sort()

        # Notify about the clues
        print(f"{' '.join(clues)}")
        guess_number += 1  # and move to the next guess
    else:
        print(
            """
-------------------------------------------------------------------------------
Sorry, you didn't get it this time.
The secret number was: {}
-------------------------------------------------------------------------------
            """.format(
                int(secret_number),
            )
        )
    return guessed


def main():
    """Run the game."""
    game(show_instructions=True)

    while True:
        answer = input("Do you want to play again? (Y/N): ")

        if answer == "N":
            print("\nThanks for playing. See you again! Bye!")
            break
        elif answer == "Y":
            game(show_instructions=False)
        else:
            print("I don't understand. Type 'Y' or 'N'.")


# Define what to do if the module is run instead of imported
if __name__ == "__main__":
    main()
