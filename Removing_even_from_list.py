x = []
print("Enter 0 to terminate")
a = input("Enter a collection of numbers: ")
for i in a:
    if int(i) % 2 == 1:
        x.append(int(i))
    else:
        pass
print(x)