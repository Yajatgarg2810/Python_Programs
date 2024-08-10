import random

def guess_number():
    # Generate a random integer between 1 and 20 inclusive
    rand_number = random.randint(1, 50)

    # Initialize an empty list to store the player's guesses
    list_of_guesses = []

    # Allow the player to make guesses until guess is equal to rand_number
    while True:

        # Prompt the player to guess an integer between 1 and 20
        # Take the player's guess and store it as a variable named guess
        guess = int(input("Guess an integer between 1 and 50: "))

        # Add the player's guess to the list_of_guesses
        list_of_guesses.append(guess)

        # Compare guess with rand_number
        if guess > rand_number :
            print("The guess is too high!")
        elif guess < rand_number:
            print("The guess is too low!")
        else:
            print("You got it!")
            break

    # Print the list of guesses
    print("You guessed the following numbers: ", list_of_guesses)
            

guess_number()