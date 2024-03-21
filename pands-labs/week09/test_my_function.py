
import logging


import my_fib_function

print(my_fib_function.fib(7))

#Test cases

assert(my_fib_function.fib(7)) == [1, 1, 2, 3, 5, 8, 13] , "incorrect return for 7"
assert(my_fib_function.fib(1)) == [1] , "incorrect return for 0"

try:
    my_fib_function.fib(-1) # Attempt to do this block of code, if everything goes fine, no errors are raised, then it doesn't move onto except
except ValueError: #If an error is raised, move onto the except statement. If an exception occurs, and its a value error, then it will do this  
    print("A value error occured")
else: # If any other error occurs, it carries the code under the else statement 
    assert False, "This did not error but it should have given a Value Error, hmmmm"

