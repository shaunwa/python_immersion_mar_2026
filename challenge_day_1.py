import random

# Select a random number between 1 and 10 (inclusive)
chosen_number = random.randint(1, 10)
print(f"(The number is {chosen_number})")

print("I'm thinking of a number between 1 and 10 (inclusive). What is it?")
game_should_continue = True # A boolean variable that controls the game loop
guesses_remaining = 5

while game_should_continue:
    try:
        user_guess = int(input(f"Enter your guess ({guesses_remaining} guesses remaining): "))

        # Check the user's guess
        if user_guess == chosen_number:
            print("That's correct! Congratulations")
            game_should_continue = False # End the game
        else:
            print("Nope! That's not it")

    except ValueError:
        print("That's not a valid number! What a waste of a turn...")

    guesses_remaining -= 1

    if guesses_remaining <= 0:
        print("You're out of turns, you lose!")
        game_should_continue = False