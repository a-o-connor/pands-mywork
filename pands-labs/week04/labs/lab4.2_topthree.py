#Write a program generates 10 random numbers (0-100) ,
#prints them out then prints out the top three.

import random

#initialise an empty list 
# numbers = []
# #initialise the variable 
# number = random.randint(0,100)
# #if the list has less than 10 integers in it
# while len(numbers) <= 10:
#       #Append to the list
#       numbers.append(number)
#       #generate a new random number
#       number = random.randint(0,100)

# #Return 3 random integers from this list 
# print("The top three are ", random.sample(numbers, k=3))

#Rewrite the above to allow the user to choose the ranges and the amount to reutrn. 

# list_length = int(input("What length should the list be?"))
# range_from = int(input("Starting range of numbers to choose from: "))
# range_to = int(input("End of range of numbers to choose from: "))
# how_many_numbers = nt(input("How many numbers to return: "))

#initialise the empty list to append to:
numbers = []

#use a for loop this time to append to this list 
for i in range (0,10):
    numbers.append(random.randint(0,100))

print(numbers)