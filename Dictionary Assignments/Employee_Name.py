n = int(input("Enter the number of employees: "))
x = []
empdict = {}    
for i in range(n):
    name = input("Enter name of the employee: ")
    number = float(input("Enter phone number of the employee: "))
    empdict[name] = number
for key in empdict:
    x.append(key)
x.sort()
dict0 = {}
for i in x:
    print(i, empdict[i])