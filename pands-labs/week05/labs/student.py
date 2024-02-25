#A program that stores a student name and a list of her courses and
# grades in a dict, the program should then print out her data.
# The number of course she has could change.

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


print("{name} got a grade of {grade} in their {course} course"
      .format(name = student["Name"], 
              course = student["Modules"][0]["Course"], 
              grade = student["Modules"][0]["Grade"]))
