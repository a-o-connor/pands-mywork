#Program that prompts user to guess a number
#Modify to tell the user if their choice  is too low or too high! 

# pick_a_number = int(input("Pick a number... "))


# while pick_a_number != 42:
#     if pick_a_number > 42:
#         print("Too high!")
#     else: print("Too low")
#     pick_a_number = int(input("Pick a different number: "))

# print("Correct!")

#Get the program to generate a random number to guess
#import random 

import random

#assign a variable to the random number
random_number = random.randint(0, 100)
print(random_number)

pick_a_number = int(input("Pick a number between 0 and 100... "))


while pick_a_number != random_number:
    if pick_a_number > random_number:
        print("Too high!")
    else: print("Too low")
    pick_a_number = int(input("Pick a different number! "))

print("Correct!")