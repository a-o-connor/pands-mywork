#Program that  prints out a random number
#import the module random from Anaconda
import random 
#Create inputs for user to specify range for random number generator: 
lower = int(input("Generate a random number between "))
upper = int(input("and "))
number = random.randint(lower, upper)
print("Here you go! " + str(number))