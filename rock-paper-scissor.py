import random

choices = ('r', 'p', 's')
emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}

while True:
    user_choice = input("Rock,Paper, or Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie")
    elif (
            (user_choice == 'r' and computer_choice == 's') or
            (user_choice == 'p' and computer_choice == 'r') or
            (user_choice == 's' and computer_choice == 'p')):
        print("You won")
    else:
        print("You lose")

    user_input = input("Continue? (y/n): ").lower()

    if user_input == 'y':
        continue
    elif user_input == 'n':
        break
    else:
        print("Invalid choice")
        break


