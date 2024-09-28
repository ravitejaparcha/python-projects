import random

num = random.randint(1,100)

while True:

    try:
        user_input = int(input("Guess the number between 1 and 100: "))

        if user_input > num:
            print("Too high!")
        elif user_input < num:
            print("Too low!")
        elif user_input == num:
            print("Congratulations! You guessed the number!")
            break

    except ValueError as ve:
        print("Please enter a valid number")



