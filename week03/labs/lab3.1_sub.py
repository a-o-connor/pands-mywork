#Program that reads in two numbers and subtracts the first one from the second one
#Author AOConnor 
#First, two inputs that ask the user to enter the first number and the second number
#Accept integers only: int()
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
#A function that subtracts first number from second number
answer = number1 - number2
print(f"{number1} minus {number2} is {answer}")