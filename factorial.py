# number to find the factorial of
number = 10 # CHANGE THIS NUMBER TO FIND ITS FACTORIAL (HERE, number=x, factorial=x!)  

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:
    # multiply the product so far by the current number
     product *= current
    
    # increment current with each iteration until it reaches number
     current += 1


# print the factorial of number
print(str(number)+'! = '+str(product))