import random
import math

print("Welcome to the number guessing game:")
print("I am thinking of a number between 1 and 100.")

# Generate the random number
actual_answer = random.randint(1, 100)

# Function to check user's guess
def check_answer(user_guess, actual_answer):
    if user_guess < actual_answer:
        print("Your guess is low, choose another number:")
        return False
    elif user_guess > actual_answer:
        print("The guess is high, make another one:")
        return False
    else:
        print("You guessed right, hurray you win!")
        return True

# Main game loop
while True:
    try:
        user_guess = int(input("Make a guess: "))
        if check_answer(user_guess, actual_answer):
            break
    except ValueError:
        print("Please enter a valid number.")

print("Program executed successfully.")






# # first thing is a header line
# import random
# import math


# print("Welcome to the number guessing game:")
# print("I am thinking of a number between 1 and 100.")

# User_guess= int(input("Make a guess: "))


# #function to guess user's guess
# def check_answer(User_guess, actual_answer):
#     if User_guess < actual_answer:

#         print("Your guess is low, choose another number:")

#     elif User_guess > actual_answer:
#         print("The guess is high, make another one:")

#     else:
#         print("You guessed right, hurray you win!")

# actual_answer= math.floor(random.randint(1,100) )

# #choosing a random number between 1 and 100


# print("Program executed successfully.")






# #taking input for difficulty

