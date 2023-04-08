# Ask user if they have played before

instructions = input("Have you played 'Lucky Unicorn' before: (Yes or No): ").lower()

# If they say yes, skip instructions

if instructions == 'yes' or instructions == 'y':
    print("Program continues")

# If no, provide instructions

elif instructions == 'no' or instructions == 'n':
    print("Provides Instructions")

# Else, re-enter question

else:
    print("re-enters question")

print(f"You have entered '{instructions}'")
