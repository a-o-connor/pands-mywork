#Program that reads in name and age and says "Your name is X and your age is Y" or something along those lines.. 
#First input: What is your name?
name = input("What is your name?")
#Second input: What age are you? Only accepts numbers!
age = int(input("What age are you?"))
#Then print out a respnse after getting the answer from the user, say Hello name , you are age. \t adds a tab space before you are age
print(f"Hello {name}, \t you are {age}")