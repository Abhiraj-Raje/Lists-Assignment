x = []
a = 1
while a >= 0:
    a = int(input("Enter a number: "))
    if a == -1:
        break
    else:
        x.append(a)
for i in range(0,len(x),4):
    if i + 2 < len(x):
        x[i],x[i+2] = x[i+2],x[i]
    if i + 3 < len(x):
        x[i+1],x[i+3] = x[i+3],x[i+1]
print(x)