"""Lucky Unicorn base component  - based on 00_Lucky_Unicorn_v1
Components added after they had been created and tested & failed
"""
import random


# Yes no Function:
def yes_no(question_text):
    while True:



        # Ask user if they have played before
        answer = input(question_text).lower()

        # If they say yes, skip instructions
        if answer == 'yes' or answer == 'y':
            answer ='yes'
            return answer

        # If no, provide instructions
        elif answer == 'no' or answer == 'n':
            answer = 'no'
            return answer

        # Else, re-enter question

        else:
            print("Please answer 'yes' or 'no'")


# Function to display instructions:
def instructions():
    print("***** HOW TO PLAY *****")
    print()
    print("The rule fo the game will go here")
    print()
    print("Program continues")
    print()


# number checking Function
def number_check(question, low, high):
    error = "That wasn't a valid input\n" \
            "Please enter a whole number between {} and {}\n".format(low, high)

    # Keep asking until valid amount
    while True:
        try:
            # ask for valid amount
            response = int(input(question))

            # check for number in the required range
            if low <= response <= high:
                return response
            else:
                print("error")
                print("Please enter a whole number between 1 & 10")

        except ValueError:
            print("error\nPlease enter a whole number between 1 & 10")


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


# Main Routine:
played_before = yes_no("Have you played Lucky Unicorn before?: ")

if played_before == "No":
    instructions()

starting_balance = number_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print("Goodbye, and have a good day!")