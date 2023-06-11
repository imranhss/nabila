import random

def display_details():
    # Displaying personal details
    print("File : wayby001_my_wordle.py")
    print("Author : Batman")
    print("Stud ID : 0123456X")
    print("Email ID : wayby001")
    print("This is my own work as defined by the University's Academic Misconduct Policy.")
    print("---------------------------------")
    print("--         My Wordle!          --")
    print("-- Guess the Wordle in 6 tries --")
    print("---------------------------------")
    print()

def get_wordle_guess(word_list):
    guess = input(f"Please enter your guess - attempt {attempt}:")

    # Validating the user's guess
    while len(guess) != 5 or guess not in word_list:
        if len(guess) != 5:
            print("Five letter words only please.")
        else:
            print("Not in word list!")
        guess = input(f"Please enter your guess - attempt {attempt}: ")

    return guess

def create_word_list():
    # Creating a list of words from the word file
    with open("word_file.txt", 'r') as infile:
        string = infile.read()
    word_list = string.split(" ")
    return word_list

display_details()

word_list = create_word_list()  # List of words read from the file

games_played = 0  # Total number of games played
wordles_solved = 0  # Number of wordles solved
wordles_unsolved = 0  # Number of wordles unsolved

play_my_wordle = input("Would you like to play My Wordle [y|n]? ")

while play_my_wordle.lower() != 'y' and play_my_wordle.lower() != 'n':
    play_my_wordle = input("Would you like to play My Wordle [y|n]? ")

while play_my_wordle.lower() == 'y':
    games_played += 1

    wordle = random.choice(word_list)  # Randomly selected wordle
    print("Wordle is:", wordle)
    print("-------------")
    print("|", " - ".join([""] * (len(wordle)+1)), "|")

    attempt = 1  # Current attempt number
    used_letters = []  # List of used letters in all attempts
    correct_letters = []  # List of correct letters guessed

    while attempt <= 6:
        guess = get_wordle_guess(word_list)  # User's guess for the wordle
        # guess = input(f"Please enter your guess - attempt {attempt}: ")
        print("-------------")
        print("|", " ".join(list(guess)), "|")

        correct_spot = 0  # Number of correct letters in correct positions
        wrong_spot = 0  # Number of correct letters in wrong positions

        # Checking if the guess is the same length as the wordle
        if len(guess) == len(wordle):
            for i in range(len(guess)):
                if guess[i] == wordle[i]:
                    correct_spot += 1
                    correct_letters.append(guess[i])
                elif guess[i] in wordle:
                    wrong_spot += 1

        used_letters.extend(guess)

        # Displaying the result of the guess
        print("|", " ".join(["^" if guess[i] == wordle[i] else "*" if guess[i] in wordle else "-" for i in range(len(wordle))]), "|")
        print("|")
        print("| Correct spot(^):", correct_spot)
        print("| Wrong spot(*):", wrong_spot)
        print("|")
        print("| Correct letters:", " ".join(correct_letters))
        print("| Used letters:", " ".join(used_letters))

        if guess == wordle:
            print(f"Solved in {attempt} tries! Well done!")
            wordles_solved += 1
            break

        attempt += 1

    if guess != wordle:
        print("Oh no! Better luck next time!")
        wordles_unsolved += 1

    play_my_wordle = input("Would you like to play again [y|n]? ")

    while play_my_wordle.lower() != 'y' and play_my_wordle.lower() != 'n':
        play_my_wordle = input("Would you like to play again [y|n]? ")

print("My Wordle Summary")
print("=================")
print(f"You played {games_played} games:")
print(f"|--> Number of wordles solved: {wordles_solved}")
print(f"|--> Number of wordles unsolved: {wordles_unsolved}")
print("Thanks for playing!")
