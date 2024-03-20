
balance = 100

def withdraw(amount):
    global balance
    if amount < 0:
        raise ValueError("This amount must be greater than 0")
    balance = balance - amount 
    return balance



if __name__=="__main__": #Lines below this will only be run when you run the module directly
    amount_to_withdraw = int(input("How much would you like to withdraw?"))
    print(withdraw(amount_to_withdraw))
    
if __name__=="__main__":
    assert withdraw(20) == 80 , "incorrect calculation" # Ensure that withdraw(20) gives 80 and if it isn't resturn an assert error with a message "incorrect calculation"
