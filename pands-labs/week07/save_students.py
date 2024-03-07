
#A program that allows a user to create new students, view and save students


#First function is called menu
def menu(): 
    print("You have chosen death \t")
    print("Type (a) to add new students \t")
    print("Type (v) view students \t")
    print("Type (q) to quit \t")
    print("Type (s) to save \t")
    choice = input(": ")
    return choice #Returns the variable from the input called choice

#Function to add modules: will be called in the add students and modules func. 
def add_modules():
    modules = [] #Initialise an empty list
    
    module_name = input("Name of module:(Blank to exit) ").strip() #Initialise a variable 
                                                                #module_name is user input of module name
    
    while module_name != "": #While the input is not blank
        new_module = {} # Do Something: create an empty dictionary
        new_module["Module name"] = module_name
        new_module["Module grade"] = input("Grade: ")#user input: module grade
        modules.append(new_module) #Add dictionary to the modules empty list 
        module_name = input("Next module:(Blank to exit) ").strip() #Update the variable
    
    return(modules) #Function returns the list of modules

#Function to add students and modules
def add_student_and_module(student_and_module):
    new_student = {}
    new_student["Name"] = input("Name of student: ")
    new_student["Modules"] = add_modules() # List of modules returned by the function
    student_and_module.append(new_student) #student_and_module will have to be a list! 

    return new_student

#Function to view students
def do_view(rats): #A new function for if they want to view a student
    print(rats)

#Function to save students
def save_student(dict):
    import json 
    with open ("saved_students.json", "w") as s:
        json.dump(dict, s)

############### MAIN PROGRAM #####################
     
#Initialise an empty list
Students = []

#A while loop!
choice = menu() #Define the variable. 
# In this case the variable is whatever the user inputs 
# in the choice input that is returned by the menu() function
while choice != "q": #While it is not equal to q
    if choice == "a":#if it is equal to a
        add_student_and_module(Students) #Carry out the add student function defined earlier 
                                        #Remember this function takes a list, we initialised an empty list 
    elif choice == "v": #if it is v
        do_view(rats = Students) #carry out the do_view function defined earlier
    elif choice == "s":
        save_student(Students)
    elif choice != "q": #if it is niether of those and also not q
        print("Please choose a, v or q") # Print out a thing to tell them they're dumb
    
    choice = menu() #update the variable. In this case, it is still the menu function 





