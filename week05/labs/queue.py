#A programe that put 10 random numbers into a queue
#Then output the values in the queue


#Create an empty list called queue
queue = []

#Get 10 random numbers 
#import random

import random

#Generate a random numbers to put in the queue
number = random.randint(0,100)

#Only want to add to the queue if it is less that 10 numbers long:  
while len(queue) < 10:
    #Append number to the list:
    queue.append(number)
    #update the variable number to a new random number
    number = random.randint(0,100)
print(queue)

#while there are still numbers in the queue

#For each number in the queue
# for number in queue:
#         print(number)
#         queue.remove(number) #Remove the number that is listed from the queue
#         print(f"Current number is {number} \t The queue is {queue}") #Print the message

#For loop doesn't work

    
#while there is number in the list 
while len(queue) != 0: # while list has stuff in it
    number = queue.pop(0) #do something & updates the variable
    print(f"Current number is {number} \t The queue is {queue}") #do something
print("Queue is empty now??")