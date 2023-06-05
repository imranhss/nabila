# question 06
import random

user_choice=int(input("Plse enter 1 for Rock, 2 for Paper and 3 for Scissors \n"))

selection = ['Rock', 'Paper', 'Scissors']
if user_choice in [1,2,3]:
    print("Your chose is ", selection[user_choice-1])

random_choice=random.randint(1,3)
if random_choice in [1,2,3]:
    print("Computer chose is ", selection[random_choice-1])


if user_choice== random_choice:
    print("Draw - no winner!")
elif user_choice==1 and random_choice==3:
    print("You Win-Paper Rock crushes scissors")
elif user_choice==2 and random_choice==1:
    print("You Win- Paper covers rock")
elif user_choice==3 and random_choice==2:
    print("You Win-Scissors cut paper")    
elif user_choice==2 and random_choice==3:
    print("You lose-Scissors cut paper")
elif user_choice==1 and random_choice==2:
    print("You lose-Paper covers rock")
elif user_choice==3 and random_choice==1:
    print("You lose-Rock crushes scissors")



 