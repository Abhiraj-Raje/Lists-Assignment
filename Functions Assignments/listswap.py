x = []
y = []
m = int(input("Enter number of elements: "))
if m % 2 == 0:
    for i in range(m):
        l = input("Enter input: ")
        x.append(l)
    for i in range(m):
        if i%2 == 0:
            y.insert(i+1, x[i])
        elif i%2 == 1:
            y.insert(i-1,x[i])
    print(y)
else:
    print("Enter even number of elements")
