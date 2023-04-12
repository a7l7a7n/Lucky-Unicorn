"""Component 3 (v3)
Generates Random token, calculates user balance, changes winnings amounts. This 'v' has an increased chance of the house winning"""

import random


starting_balance = 100
balance = starting_balance


# testing loop (100) tokens
for item in range(10):
    number = random.randint(1,100)
    token = random.randint(1, 100)

    # Adjust balance
    # If integer is between 1 and 5, +$4 to user_balance
    if 1 <= number <= 5:
        token == "unicorn"
        balance += 4
    # if integer is between 6 and 36, -$1 from user_balance
    elif 6 <= number <= 36:
        token == "donkey"
        balance -= 1

    else:
        # if integer is more than 36 and divisible by 2 then -0.50c from user_balance
        if number % 2 == 0:
            token == "zebra"
            balance -= 0.5

        # if integer is more than 36 and not divisible by 2 then -0.50c from user_balance
        else:
            token == "horse"
            balance -= 0.5

    print(f"Token: {token}, Balance: ${balance:.2f}")

# output
print()
print(f"Starting balance = ${starting_balance:.2f}")
print(f"Final balance = ${balance:.2f}")
