x = []
largest_num = 0
second_largest_num = 0
a = 1
while a >= 0:
    a = int(input("Enter a number: "))
    if a == -1:
        break
    else:
        x.append(a)
for i in x:
    if i > largest_num:
        largest_num = i
x.remove(largest_num)
for i in x:
    if i > second_largest_num:
        second_largest_num = i
print("Largest num:",largest_num)
print("Second largest num",second_largest_num)