x = []
y = []
a = 1
while a >= 1:
    a = int(input("Enter a number: "))
    if a == 0:
        break
    else:
        x.append(a)
m = len(x)
for i in range(0, m):
    y.append(min(x))
    x.remove(min(x))
print(y)