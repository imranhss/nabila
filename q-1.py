# question 01 
def determine_grade(score):
    if score <0:
        return "Invalid Number"
    elif score <=39:  # if score <=39:
        return "F2"
    elif score <=49:
        return "F1"
    elif score <=54:
        return "P2"
    elif score <=64:
        return "P1"
    elif score <=74:
        return "C"
    elif score <=84:
        return "D"
    elif score <=100: # else: 
        return "HD"   # return "HD"
    else:
        return "Invalid Number"


print(determine_grade(-600))
     
