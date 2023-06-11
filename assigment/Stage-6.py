import random

word_list = ["woods", "times", "pumps", "relic", "smoke", "cards", "slate", "tonic",
"solid", "speak", "wants", "angle", "adapt", "apple", "smart", "gates",
"water", "hagle", "honey", "other", "table", "fakes", "sully", "flesh",
"sheer", "tense", "tease", "drake", "rains", "stone", "phone", "flown",
"glass"]

play_my_wordle = 'y'

while play_my_wordle.lower() == 'y':
    wordle = random.choice(word_list)
    print("Wordle is:", wordle)
    print("-------------")
    print("|", " - ".join([" "] * len(wordle)), "|")

    attempt = 1

    while True:
        guess = input(f"Please enter your guess - attempt {attempt}: ")
        print("You guessed:", guess)
        feedback = []
        correct_spot = 0
        wrong_spot = 0

        for i in range(len(wordle)):
        # if guess[i] not in word:    
            if guess[i] == wordle[i]:
                feedback.append("^")
                correct_spot += 1
            elif guess[i] in wordle:
                feedback.append("*")
                wrong_spot += 1
            else:
                feedback.append("-")
        print("-------------")
        print("|", " ".join(list(guess)), "|")
        print("| {} |".format(" ".join(feedback)))
        
        
        # print("|", " ".join(list(guess)), "|")
        # print("|", " ".join(["*"] if i in correct_positions else "-" for i in range(len(wordle))), "|")
        # print("|", " ".join(["^"] if i in wrong_positions else "-" for i in range(len(wordle))), "|")
        # print("|", " ".join(["^" ]if i in missing_positions else "-" for i in range(len(wordle))), "|")

        if guess == wordle:
            print("Congratulations! You guessed the word correctly!")
            break

        attempt += 1

    
    play_my_wordle = input("Would you like to play My Wordle [y|n]? ")

print("Thanks for playing!")



# End of stage 5