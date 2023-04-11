"""Component 3 (v2)
Generates Random token and calculates user balance"""

import random

tokens = ["unicorn", "horse", "zebra", "donkey"]
balance = 100


# testing loop
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')

    # adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "horse":
        balance -= .50
    elif token == "zebra":
        balance -= .50
    else:
        balance -= 1

print(f"Token: {token}, Balance: ${balance}")
