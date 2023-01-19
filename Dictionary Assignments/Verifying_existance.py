dict1 = {}
x = ()
y = ()
ch = 'y'
while ch == 'y':
    key = input("Enter key: ")
    val = input("Enter value: ")
    dict1[key] = val
    ch = input("Enter y to continue: ")
    if ch != 'y':
        break
x = list(dict1.keys())
y = list(dict1.values())
a = input("Enter the value you wanna find: ")
if a in y:
    print(x[y.index(a)])
else:
    print("value not found")