import random

def generate_number():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    selection = ['Rock', 'Paper', 'Scissors']

    print("Your choice is", selection[user_choice-1])
    print("Computer's choice is", selection[computer_choice-1])

    if user_choice == computer_choice:
        print("Draw - no winner!")
    elif user_choice == 1 and computer_choice == 3:
        print("You Win - Rock crushes Scissors")
    elif user_choice == 2 and computer_choice == 1:
        print("You Win - Paper covers Rock")
    elif user_choice == 3 and computer_choice == 2:
        print("You Win - Scissors cut Paper")
    else:
        print("You lose!")

def play_game():
    play_again = 'y'
    games_played = 0

    while play_again.lower() == 'y':
        user_choice = int(input("Please enter 1 for Rock, 2 for Paper, and 3 for Scissors: "))
        computer_choice = generate_number()
        determine_winner(user_choice, computer_choice)
        games_played += 1
        play_again = input("Play again? (y/n): ")

    return games_played

num_games = play_game()

if num_games == 1:
    print("You played 1 game!")
else:
    print("You played", num_games, "games!")

print("Thanks for playing!")
