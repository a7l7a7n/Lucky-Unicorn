"""Component 3 (v1)
Generates Random token"""

import random

tokens = ["unicorn", "horse", "zebra", "donkey"]

# testing loop
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')
