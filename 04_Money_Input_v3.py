""" User's Balance v3
This addition make sure when the user puts in a letter or a non-whole number the program doesn't crash."""

error = "That wasn't a valid input\n"
user_balance = 0

# Keep asking until valid amount
while not 1 <= user_balance <= 10:
    try:
        #ask for valid amount
        user_balance = int(input("Please enter a whole number between 1 & 10"
                                 "\nHow much would you like to play with? $"))

        print()

    except ValueError:
        print("error")

print(f"You are playing with ${user_balance}")
