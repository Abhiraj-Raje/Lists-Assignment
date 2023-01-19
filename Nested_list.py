#Algorithm
#Take an initial input list
#After that list is ended, append that in another list
x = []
y = []
a = 0
while a >= 0:
    while a >= 0:
        a = input("Enter a number: ")
        if a == '':
            break
        else:
            y.append(int(a))
    x.append(y)