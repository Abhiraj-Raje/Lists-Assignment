num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
def arops(a,b):
    add = a + b
    sub = a-b
    mul = a*b
    power = a^b
    if b!= 0:
        div = a/b
    else:
        div = "Division by 0 is not possible"
    return add,sub,mul,power,div
print(arops(num1,num2))