import random
n1 = int(input("Enter first limit: "))
n2 = int(input("Enter second limit: "))
def numbergen(a,b):
    num1 = random.randint(a,b)
    num2 = random.randint(a,b)
    num3 = random.randint(a,b)
    return num1,num2,num3
print("The numbers are: \n",numbergen(n1,n2))