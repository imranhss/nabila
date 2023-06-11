import random

word_list = ["woods", "times", "pumps", "relic", "smoke", "cards", "slate", "tonic",
"solid", "speak", "wants", "angle", "adapt", "apple", "smart", "gates",
"water", "hagle", "honey", "other", "table", "fakes", "sully", "flesh",
"sheer", "tense", "tease", "drake", "rains", "stone", "phone", "flown",
"glass"]

play_again = 'y'
attempt = 1

while play_again.lower() == 'y':
    wordle = random.choice(word_list)
    print("Wordle is:", wordle)
    print("-------------")
    print("|", " ".join(["-"] * len(wordle)), "|")

    guess = input(f"Please enter your guess - attempt {attempt}: ")
    print("You guessed:", guess)

    play_again = input("Would you like to play again [y|n]? ")

    attempt += 1

print("Thanks for playing!")


# End of stage 3