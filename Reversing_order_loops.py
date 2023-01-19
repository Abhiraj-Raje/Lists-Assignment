x = []
z = []
a = 1
while a >= 1:
    a = int(input("Enter a number: "))
    if a == 0:
        break
    else:
        x.append(a)
for i in range(0, len(x)):
    y = x[len(x) - 1 - i]
    z.append(y)
print(z)