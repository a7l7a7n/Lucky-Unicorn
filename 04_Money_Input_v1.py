""" User's Balance v1
This code asks the user if they want to play and how much they are willing to spend (the minimum amount is 1 and the
maxium is 10). This is put into the 'users balance'."""

user_balance = int(input("How much money do you want to play with (must be a hole number between 1 but less that 10: " ))

# keep asking if number not between 1 and 10
while not 1 <= user_balance <=10:
    print("error, please enter a whole number between 1 and 10")
    #ask again
    user_balance = int(input("How much $money$ do yo want to play with? "))

print(f"you are playing with ${user_balance}")