x = []
y = []
a = 1
while a >= 0:
    a = int(input("Enter a number: "))
    if a == -1:
        break
    else:
        x.append(a)
search = int(input("Enter the number you wanna find"))
freq_num = 0
position = 0
if search not in x:
    print("Number not found")
else:
    for i in x:
        position = position + 1
        if search == i:
            freq_num = freq_num + 1
            y.append(position)
    print("Frequency",freq_num)
    print("The position is",y)