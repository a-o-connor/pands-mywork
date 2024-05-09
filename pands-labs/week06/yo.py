 
#A program that allows a user to create new students, and view students, in the dict object

#The student dictionary object
# student = {
#     "Name": "Mary",
#     "Modules":[
#         {
#         "Course":"Programming",
#         "Grade":45,
#     },
#     {
#         "Course":"History",
#         "Grade": 99
#     } 
#     ]
# }

#First function is called menu
def menu(): 
    print("You have chosen death \t")
    print("Type (a) to add new students \t")
    print("Type (v) view students \t")
    print("Type (q) to quit")
    choice = input(": ")
    return choice #Returns the variable from the input called choice


def add_modules():
    modules = []
    module_name = input("Name of module:(Blank to exit) ").strip()
    
    while module_name != "":
        new_module = {}
        new_module["Module name"] = module_name
        new_module["Module grade"] = input("Grade: ")
        modules.append(new_module)
        module_name = input("Next module:(Blank to exit) ").strip()
    
    return(modules)


def add_student_and_module(student_and_module):
    new_student = {}
    new_student["Name"] = input("Name of student: ")
    new_student["Modules"] = add_modules()
    student_and_module.append(new_student)

    return new_student


def do_view(rats): #A new function for if they want to view a student
    print(rats)
    for rat in rats:
     print(rats[0]["Modules"])

Students = []

#A while loop!
choice = menu() #Define the variable. 
# In this case the variable is whatever the user inputs 
# in the choice input that is returned by the menu() function
while choice != "q": #While it is not equal to q
    if choice == "a":#if it is equal to a
        add_student_and_module(Students) #rry out the add student function defined earlier
    elif choice == "v": #if it is v
        do_view(rats = Students) #carry out the do_view function defined earlier
    elif choice != "q": #if it is niether of those and also not q
        print("Please choose a, v or q") # Print out a thing to tell them they're dumb
    choice = menu() #update the variable. In this case, it is still the menu function 

print(Students)
