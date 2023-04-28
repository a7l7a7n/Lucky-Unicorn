"""Not the Final program"""


# Yes no Function:
def yes_no(question_text):
    while True:
        # Ask user if they have played before
        answer = input(question_text).lower()

        # If they say yes, skip instructions
        if answer == 'yes' or answer == 'y':
            answer = 'yes'
            print("program continues")

        # If no, provide instructions
        elif answer == 'no' or answer == 'n':
            answer = 'no'
            print("***** HOW TO PLAY *****")
            print()
            print("The rule fo the game will go here")
            print()

        # Else, re-enter question

        else:
            print("Please answer 'yes' or 'no'")



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


#Main Routine:
instructions = yes_no("Have you played Lucky Unicorn before?: ")
print(f"You have entered '{instructions}'")
user_balance = number_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance}")

