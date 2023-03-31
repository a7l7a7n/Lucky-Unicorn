# Ask user if they have played before

instructions = input("Have you played 'Lucky Unicorn' before? (Yes or No): ")

# If they say yes, skip instructions

if instructions == 'Yes' or instructions == 'yes':
    print("Program continues")

# If no, provide instructions

elif instructions == 'No' or instructions == 'no':
    print("Provides Instructions")

# Else, re-enter question

else:
    print("re-enters question")
