# Messing with variable types 
# Author: A O'Connor
answer = int(1)
print(answer)
answer2 = ("12")
print(f"answer is {answer2}")
print(f"answer is {answer}")

#print("answer is " + answer)
# Did not work because "answer" variable is an integer that cannot be concatenated into a string 
# check the type: 
print(type(answer))
print("answer is " + str(answer))