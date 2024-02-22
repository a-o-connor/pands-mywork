#Take in an amount in the form -x.xx and convert to xxx
#takes in a float amount of dollars and returns that absolute amount in cent
floatnum = float(input("Enter amount in $: "))
absolutenum = abs(floatnum)
incents = absolutenum*100
print("That amount in cents is: " + str(incents))

