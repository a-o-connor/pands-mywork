#A program that reads in numbers 
#Until the user presses 0 to quit
#Then returns the list of numbers
#and average of the numbers input

#Initialise an empty list 
numbers = []

#Initialise the variable 
number = int(input("Input a number (or press 0 to quit): "))

#Check if the number is 0
while number != 0:
    #Do something!
    numbers.append(number)
    #Change the variable
    number = int(input("Input a number (or press 0 to quit): "))

import statistics

for number in numbers:
    print(number)

averaged_numbers = statistics.mean(numbers)
print("The average of these numbers is ", averaged_numbers)