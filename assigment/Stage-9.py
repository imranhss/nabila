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
    used_letters = []
    correct_letters = []

    while attempt <= 6:
        guess = input(f"Please enter your guess - attempt {attempt}: ")
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
            break

        attempt += 1

    if attempt > 6:
        print("Oh no! Better luck next time!")
        print(f"The wordle was: {wordle}")

    play_my_wordle = input("Would you like to play again [y|n]? ")

print("Thanks for playing!")



# End of stage 9