import random
import string

def generate_password(length):    
    letters = string.ascii_letters
    result = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result)

generate_password(10)


