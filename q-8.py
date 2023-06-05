import random
import string

length=int(input("Please enter ur password length "))

def generate_password():    
    letters = string.ascii_letters
    result = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result)

generate_password()

