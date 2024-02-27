
#A program that allows a user to create new students, and view students, in the dict object

#The student dictionary object
student = {
    "Name": "Mary",
    "Modules":[
        {
        "Course":"Programming",
        "Grade":45,
    },
    {
        "Course":"History",
        "Grade": 99
    } 
    ]
}

#First function is called menu
def menu(): #How many arguments does it take? 
    print("You have chosen death \t")
    print("Type (a) to add new students \t")
    print("Type (v) view students \t")
    print("Type (q) to quit")
    choice = input(": ")
    return choice #Returns an input called choice

def do_add(): #A new function for if they want to add a student
    # print("kffkfkfkkddkd")
    student_name = input("Please enter the student's name: ")
    student_course = input("Please enter the student's course: ")
    student_grade = input("Please enter the student's grade: ")
    # return(student_name, student_course, student_grade)

def do_view(): #A new function for if they want to view a student
    print("View students on your own time")

#A while loop!
choice = menu() #Define the variable. In this case the variable is our function
while choice != "q": #While our function (which returns an input of a user typing something!) is not equal to q
    if choice == "a":#if it is a  
        do_add() #carry out the do_add function defined earlier
    elif choice == "v": #if it is v
        do_view() #carry out the do_view function defined earlier
    elif choice != "q": #if it is niether of those and also not q
        print("Please choose a, v or q") # Print out a thing to tell them they're dumbe
    choice = menu() #update the variable. In this case, it is still the menu function 


print(do_add())
