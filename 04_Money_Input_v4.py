""" User's Balance v4
This addition make sure when the user puts in a letter or a non-whole number the program doesn't crash."""

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

        except ValueError:
            print("error")


# Main routine
user_balance = number_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance}")