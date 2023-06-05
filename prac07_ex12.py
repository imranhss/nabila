import rps_game
# Call function play_game
num_games = rps_game.play_game()
if num_games == 1:
    print("\n\nYou played", num_games, "game!")
else:
    print("\n\nYou played", num_games, "games!")
    print('\nThanks for playing!')