#Create a program to read in a users name and print out Hello name
#
#Allow the user to input their own name
name = input("Enter your name here....")
#Print out the word Hello, a space, and the name that was input 
print("Hello " + name)
#want the program to say Hello name, and then NIe to meet you on a new line 
#use print()
#use \n to go to a new line
#use {} to allow the variable name to exist within the verbatim print within the ""
print("Hello {name}, \n nice to meet you")
#ok that didn't work, {name} printed out instead of the variable name 
#f needs to be before the inverted commas to take the {} variable out of the verbatim print 
print(f"Hello {name}, \n nice to meet you")
#whoop that worked
