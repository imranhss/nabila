import random

def display_details():
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
    guess = input("Please enter your guess: ")

    while len(guess) != 5 or guess not in word_list:
        if len(guess) != 5:
            print("Five letter words only please.")
        else:
            print("Not in word list!")
        guess = input("Please enter your guess: ")

    return guess

def create_word_list():    
    infile=open("word_file.txt",'r')
    string=infile.read() 
    word_list=string.split(" ")
    return word_list

display_details()

word_list = create_word_list()

games_played = 0
wordles_solved = 0
wordles_unsolved = 0

play_my_wordle = input("Would you like to play My Wordle [y|n]? ")

while play_my_wordle.lower() != 'y' and play_my_wordle.lower() != 'n':
    play_my_wordle = input("Would you like to play My Wordle [y|n]? ")

while play_my_wordle.lower() == 'y':
    games_played += 1

    wordle = random.choice(word_list)
    print("Wordle is:", wordle)
    print("-------------")
    print("|", " - ".join([" "] * len(wordle)), "|")

    attempt = 1
    used_letters = []
    correct_letters = []

    while attempt <= 6:
        guess = get_wordle_guess(word_list)

        print("-------------")
        print("|", " ".join(list(guess)), "|")

        correct_spot = 0
        wrong_spot = 0

        if len(guess) == len(wordle):
            for i in range(len(guess)):
                if guess[i] == wordle[i]:
                    correct_spot += 1
                    correct_letters.append(guess[i])
                elif guess[i] in wordle:
                    wrong_spot += 1

        used_letters.extend(guess)

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

# End stage 15


