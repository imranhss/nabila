import random

welcome_text="""
File:wayby001_my_wordle.py
Author: Nabila Chowdhury
Stud ID: 0123456x
Email ID: wayby001
This is my own work as defined by the University's Academic Misconduct Policy.
---------------------------------
--          My Wordle!         --
-- Guess the Wordle in 6 tries --
---------------------------------
Would you like to play My Wordle [y|n]? 
"""

def create_word_list():
    infile=open("word_file.txt",'r')
    string=infile.read() 
    word_list=string.split(" ")
    return random.choice(word_list)

def check_guess(word, guess):
    if len(guess) != len(word):
        return False
    
    for i in range(len(word)):
        if guess[i] != word[i] and guess[i] not in word:
            return False
    
    return True

def display_details(word, guess):
    feedback = []
    correct_spot = 0
    wrong_spot = 0
    
    for i in range(len(word)):
        if guess[i] not in word:    
        # if guess[i] == word[i]:
            feedback.append("^")
            correct_spot += 1
        elif guess[i] in word:
            feedback.append("*")
            wrong_spot += 1
        else:
            feedback.append("-")
    
    return feedback, correct_spot, wrong_spot

def get_wordle_guess():
    word = create_word_list()
    attempts = 0
    guesses = set()
    
    print("---------------------------------")
    print("-- My Wordle! --")
    print("-- Guess the Wordle in 6 tries --")
    print("---------------------------------")
    
    play_prompt = input(welcome_text)

    
    if play_prompt.lower() != 'y':
        print("No worries... another time perhaps... :)")
        return
    
    print("Let's play My Wordle!")
    print("Guess the 5-letter word.")
    
    while attempts < 6:
        guess = input("Please enter your guess - attempt {}: ".format(attempts+1)).lower()
        
        if guess in guesses:
            print("You already guessed that word. Try again!")
            continue
        
        if len(guess) != 5:
            print("Invalid guess. Please enter a 5-letter word.")
            continue
        
        guesses.add(guess)
        attempts += 1
        
        feedback, correct_spot, wrong_spot = display_details(word, guess)
        
        print("-------------")        
        print("| {} |".format(" ".join(guess)))
        print("| {} |".format(" ".join(feedback)))
        print("|")
        print("| Correct spot(^):", correct_spot)
        print("| Wrong spot(*):", wrong_spot)
        
        if check_guess(word, guess):
            print("Congratulations! You guessed the word!")
            print("Number of attempts:", attempts)
            break
        else:
            if attempts < 6:
                print("Please guess again!")
    
    if attempts == 6 and not check_guess(word, guess):
        print("Sorry, you ran out of attempts.")
        print("The word was:", word)
    
    print("Thank you for playing My Wordle!")

get_wordle_guess()
