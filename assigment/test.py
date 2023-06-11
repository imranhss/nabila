import random

def display_wordle(wordle, guesses):
    print("-------------")
    print("|", " ".join(list(wordle)), "|")
    for i in range(len(wordle)):
        if guesses[i] == '^':
            print("|", "^", end=" ")
        elif guesses[i] == '*':
            print("|", "*", end=" ")
        else:
            print("|", "-", end=" ")
    print("|\n")

def get_wordle_guess():
    guess = input("Please enter your guess - attempt {}: ")
    print("You guessed:", guess)
    return guess

def create_word_list():
    with open('word_file.txt', 'r') as file:
        word_list = [line.strip() for line in file]
    return word_list

def play_wordle():
    word_list = create_word_list()
    num_games = 0
    num_solved = 0
    num_unsolved = 0
    play_again = 'y'

    while play_again == 'y':
        wordle = random.choice(word_list)
        guesses = ['-'] * len(wordle)
        attempts = 1
        solved = False

        print("-------------")
        print("| - - - - - |")
        print("Would you like to play My Wordle [y|n]?")
        play_again = input()

        if play_again != 'y':
            break

        num_games += 1

        while attempts <= 6 and not solved:
            guess = get_wordle_guess()

            if len(guess) != len(wordle):
                print("Invalid guess. The wordle has 5 letters.")
                continue

            for i in range(len(wordle)):
                if guess[i] == wordle[i]:
                    guesses[i] = '^'
                elif guess[i] in wordle:
                    guesses[i] = '*'
                else:
                    guesses[i] = '-'

            display_wordle(wordle, guesses)

            correct_spot = guesses.count('^')
            wrong_spot = guesses.count('*')

            print("| Correct spot(^):", correct_spot)
            print("| Wrong spot(*):", wrong_spot)

            if correct_spot == len(wordle):
                print("\n| Correct letters:", " ".join(list(wordle)))
                print("| Used letters:", " ".join(guess))
                print("\nSolved in", attempts, "tries! Well done!")
                num_solved += 1
                solved = True
            else:
                attempts += 1

        if not solved:
            print("\n| Correct letters:", " ".join([c for i, c in enumerate(wordle) if guesses[i] == '^']))
            print("| Used letters:", " ".join(guess))
            print("\nOh no! Better luck next time!")
            print("The wordle was:", wordle)
            num_unsolved += 1

    print("\nMy Wordle Summary")
    print("=================")
    print("You played", num_games, "games:")
    print("|--> Number of wordles solved:", num_solved)
    print("|--> Number of wordles unsolved:", num_unsolved)
    print("Thanks for playing!")

play_wordle()

# End stage 1 


