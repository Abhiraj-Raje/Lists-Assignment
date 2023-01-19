def get_key(num):
    for key in empdict:
        if empdict[key] == num:
            return key
    return "Key not found"
n = int(input("Enter the number of employees: "))
x = []
empdict = {}    
for i in range(n):
    name = input("Enter name of the employee: ")
    number = float(input("Enter phone number of the employee: "))
    empdict[name] = number
for val in empdict:
    x.append(empdict[val])
x.sort()
for i in x:
    print(get_key(i), i)