x = []
a = 1
while a >= 1:
    a = int(input("Enter a number: "))
    if a == 0:
        break
    else:
        x.append(a)
for i in range(0, len(x)):
    y = x.index(x[i])
    if x.count(x[i]) > 1 and i > y:
        x[i] = 0
print(x)