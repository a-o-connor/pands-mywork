#Program that reads in two numbers and divides the first one by the second and give the integer result and the remainder
#First, create two inputs for the numbers to be read in
#Accept floats: fl()
number = float(input("Enter the first number: "))
divisor = float(input("Enter the number you want to divide by: "))
#Function that divides the number by the divisor
answer = int(number/divisor)
#print(number/divisor)
#Want to print the integer result
#print(int(answer))
#Want to calculate the remainder
#Function in Python to do this: Modulus: % 
remainder = int(number%divisor)
#Want only one decimal place for this
#print(int(remainder))
print(f"{number} divided by {divisor} is {answer} with remainder {remainder}")
print("{} divided by {} is {} with remainder {}".format(number, divisor, answer, remainder))
      
      