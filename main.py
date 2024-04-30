import random

choices = ['snake', 'water', 'gun']
computer_choice = random.choice(choices)
player_choice = input("Enter your choice (snake/water/gun): ").lower()
print(f"Computer chooses: {computer_choice}")
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == 'snake':
    if computer_choice == 'water':
        print("You win!")
    else:
        print("Computer wins!")
elif player_choice == 'water':
    if computer_choice == 'gun':
        print("You win!")
    else:
        print("Computer wins!")
elif player_choice == 'gun':
    if computer_choice == 'snake':
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid input! Please enter snake, water, or gun.")
    