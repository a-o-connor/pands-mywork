#A program that stores a student name and a list of her courses and
# grades in a dict, the program should then print out her data.
# The number of course she has could change.

student = {
    "Student": "Mary",
    "Modules":[
        {
        "Programming":45,
    },
    {
        "History": 99
    } 
    ]
}

print(student["Modules"][0:len(student["Modules"])])