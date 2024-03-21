

#Define a function that returns a fibonacci sequence of n numbers:
def fib(n):
    if n < 0: 
        raise  ValueError("Must be a positive number")
    list = []
    a, b = 0, 1
    while len(list) < n:
        a, b = b, a+b
        list.append(a)
    return list


#Create a section that contains the testing code: 
if __name__ == "__main__":
    print(fib(7))
    print("This was run directly")
else:
    print("This was run from a different file")