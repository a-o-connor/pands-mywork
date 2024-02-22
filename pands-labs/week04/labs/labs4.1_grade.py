#Program that reads in a student’s percentage mark and
#prints out corresponding the grade

# • Under 40% => Fail
# • Between 40% and 49% => Pass
# • Between 50% and 59% => Merit 2
# • Between 60% and 69% => Merit 1
# • Over 70% => Distinction

#First, input the grade: 
# grade = int(input("What grade did you receive? "))

# #Check that this input is a number between 0 and 100:
# if grade > 100 or grade < 0:
#     print("Please enter a valid grade")
# elif grade < 40:
#     print("Fail")
# elif grade < 50:
#     #< does not include the number, so this will be between 40 and 49
#     print('Pass')
# elif grade < 60:
#     print('Merit 2')
# elif grade < 70:
#     print('Merit 1')
# else:
#     print("Distinction")

#Modify program to have 69.5 be rounded to 70!
    
grade = float(input("What grade? "))

#import math 

import math

#math.ceil() will return the rounded up value of a number 

rounded_grade = math.ceil(grade)


if rounded_grade > 100 or rounded_grade < 0:
    print("Please enter a valid grade")
elif rounded_grade < 40:
    print("Fail")
elif rounded_grade < 50:
    #< does not include the number, so this will be between 40 and 49
    print('Pass')
elif rounded_grade < 60:
    print('Merit 2')
elif rounded_grade < 70:
    print('Merit 1')
else:
    print("Distinction")

#A while loop that keeps prompting the user to input -1!

pick_a_number = int(input("Pick a number... "))

while pick_a_number != -1:
    print ("Try again")
    pick_a_number = int(input("Pick a different number: "))

print("Correct!")