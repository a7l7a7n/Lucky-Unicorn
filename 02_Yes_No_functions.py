
# Function:
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


#Main Routine:
instructions = yes_no("Have you played Lucky Unicorn before?\n: ")
print(f"You have entered '{instructions}'")
print()
fun = yes_no("Are you having fun?\n: ")
print(f"You have entered '{fun}'")
