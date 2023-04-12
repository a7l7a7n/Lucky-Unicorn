"""Component 4 v2 Game mechanics and looping
removed all hard-wiring so that all tokens allocated
User gives feedback about number of rounds and maintains user_balance"""

import random


# token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # testing loop to generate tokens
    while play_again != "x":
        rounds_played += 1
        number = random.randint(1, 100)

        # Adjust balance
        # if the random integer is between 1 and 5, user gets unicorn (+4 user_balance)
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4

        # if the random integer is between 6 and 36, user gets donkey (-1 user_balance)
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1

    # if the random integer is between 37 and 100, and is divisible by 2, then the user get a horse (-0.50 user_balance)
# if the random integer is between 37 and 100, and is not divisible by 2, then the user get a zebra (-0.50 user_balance)
        else:
            if number % 2 == 0:
                token = "horse"
                balance -= 0.5

            else:
                token = "zebra"
                balance -= 0.5

        # Output
        print(f"Round {rounds_played}, Token: {token}, Balance: ${balance}")
        if balance < 1:
            print("\nSorry, you have run out of money")
            play_again = "x"
        else:
            play_again = input("Press <enter> to play again or 'x' to exit the game").lower()
        print()
        return balance


# Main routine
starting_balance = 5
closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print("Goodbye, and have a good day!")
