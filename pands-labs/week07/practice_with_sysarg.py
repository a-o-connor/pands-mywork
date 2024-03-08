import sys 

args = sys.argv

n = len(args)

#dealing with the whitespaces 
for i in range(1,n):
    print(f"{args[i]}", end=" ") #The end = " " argument separates the variables by a space not a line! 

print(args)
print(args[1:])


# Dealing with errors: want to concatenate filename with a space in it into 1 variable 
# e.g. if the command line is $ es.py moby dick.txt
# args[1:] = ["moby", "dick.txt"]
# But filename variable should be "moby dick.txt"

filename = ' '.join(args[1:])

print(len(filename))
print(type(filename))
print(filename)




