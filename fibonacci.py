import random

# F means "Fibonacci"
def F(n):
    
    # there is not "0" th number in Fibonacci array
    if n < 0:
        print("It is not correct")
    # the first number is 0
    elif n == 1:
        return 0
    # the second number is 1
    elif n == 2:
        return 1
    else:
        return F(n-1)+F(n-2)

print ("Output for given number: ")
print (F(2)) 

a = random.randint(3,25)
print ("Random number is: " + str(a))
print ("Output for random number: ")
print (F(a))
