"""Component 4 v1
Game mechanics and looping
Based on 05_token_generator_v4"""

import random

# main routine
test_amount = 5
balance = test_amount

rounds_played = 0
play_again = ""

# testing loop to generate tokens
while play_again != "x":
    rounds_played += 1
    number = random.randint(6, 36)

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
        else:
            token = "zebra"

