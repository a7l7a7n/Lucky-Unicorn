""" User's Balance v2
This addition make sure when the user puts in a letter or a non-whole number the program doesn't crash."""

error = "Please enter a whole number between 1 & 10\n"
valid = False

# Keep asking until valid amount
while not valid:
    try:
        #ask for valid amount
        user_balance = int(input("How much would you like to play with? $"))

        # check if amount is valid
        if 0 < user_balance <= 10:
            print(f"You are playing with ${user_balance}")
            valid = True
        else:
            print(error)

    except ValueError:
        print("error")
