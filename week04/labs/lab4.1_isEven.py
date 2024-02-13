#Program that asks the user to enter in a number, and the
#program will tell the user if the number is even or odd.
#Author: A O'Connor

#First, an input that onle accepts integers
your_number = int(input("Please enter a number to check: "))

#Check is the number divisible by 2
#Use modulus: %
remainder = your_number%2

#If Else statement:
if remainder == 1:
    print(f"{your_number} is odd")
else:
    print(f"{your_number} is even")