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
    print("|", "-"* len(wordle), "|")

    attempt = 1

    while True:
        guess = input(f"Please enter your guess - attempt {attempt}: ")
        print("You guessed:", guess)

        correct_letters = 0
        correct_positions = []
        wrong_positions = []

        if len(guess) == len(wordle):
            for i in range(len(guess)):
                if guess[i] == wordle[i]:
                    correct_letters += 1
                    correct_positions.append(i)
                elif guess[i] in wordle:
                    wrong_positions.append(i)

        print("-------------")
        print("|", " ".join(list(guess)), "|")
        #print("|", " ".join(["*" if i in wrong_positions else " " for i in range(len(wordle))]), "|")
        #print("|", " ".join(["*" if i in correct_positions else " " for i in range(len(wordle))]), "|")
        print("|", " ".join(["*" if i in wrong_positions else " " for i in range(len(wordle))]), "|")

        if guess == wordle:
            print("Congratulations! You guessed the word correctly!")
            break

        attempt += 1

    total_letters = correct_letters + len(wrong_positions)
    print(f"{correct_letters} of {total_letters}")

    play_my_wordle = input("Would you like to play My Wordle [y|n]? ")

print("Thanks for playing!")

# End of stage 5