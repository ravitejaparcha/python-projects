import random

while True:
    user_input = input("Do you want to roll the dice?(y/n): ").lower()

    if user_input == 'y':
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)
        print(f"({num1},{num2})")
    elif user_input == 'n':
        print("Thanks for playing the dice game!")
        exit()
    else:
        print("invalid choice")

