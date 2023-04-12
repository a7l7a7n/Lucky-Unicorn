"""Component 3 (v3)
Generates Random token, calculates user balance, changes winnings amounts"""

import random

tokens = ["unicorn",
          "horse", "horse", "horse",
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey"]
starting_balance = 100
balance = starting_balance


# testing loop (100) tokens
for item in range(20):
    token = random.choice(tokens)


    # adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "horse":
        balance -= .50
    elif token == "zebra":
        balance -= .50
    else:
        balance -= 1

print(f"Starting balance = ${starting_balance:.2f}")
print(f"Final balance = ${balance:.2f}")
