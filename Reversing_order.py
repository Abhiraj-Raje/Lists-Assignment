x = []
a = 1
while a >= 1:
    a = int(input("Enter a number: "))
    if a == 0:
        break
    else:
        x.append(a)
print(x)
x.reverse()
print(x)