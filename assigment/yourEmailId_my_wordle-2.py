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
    return word_list


def check_guess(word, guess):
    if len(guess) != len(word):
        return False
    
    for i in range(len(word)):
        if guess[i] != word[i] and guess[i] not in word:
            return False
    
    return True

def get_wordle_guess(word_list):
    print(create_word_list)
    word=random.choice(create_word_list())
    attempts = 0
    guesses = set()
    print("Welcome to My Wordle!")
    print("Guess the 5-letter word.")
    while True:
        guess = input("Enter your guess: ").lower()
        
        if guess == "quit":
            break
        
        if guess in guesses:
            print("You already guessed that word. Try again!")
            continue
        
        guesses.add(guess)
        attempts += 1
        
        if check_guess(word, guess):
            print("Congratulations! You guessed the word!")
            print("Number of attempts:", attempts)
            break
        else:
            print("Incorrect guess. Try again!")
    
    print("Thank you for playing My Wordle!") 
    
    
get_wordle_guess(create_word_list())    


# user_permission=input(welcome_text)

# if user_permission.lower()== 'y':
#     user_guse=input("| - - - - - | \nPlease enter your guess - attempt 1:\n")
#     read_file(user_guse)
    
# elif user_permission.lower()=='n':
#    print("No worries... another time perhaps... :)") 