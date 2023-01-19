def sum_of_elements(list1):
    sum1 = 0
    for i in list1:
        sum1 = sum1 + i
    return sum1
n = int(input("Enter the number of students: "))
dict0 = {}
for i in range(n):
    x = []
    name = input("Enter the name of the student: ")
    phy = int(input("Enter marks in physics: "))
    che = int(input("Enter marks in chemistry: "))
    math = int(input("Enter marks in maths: "))
    eng = int(input("Enter marks in english: "))
    cs = int(input("Enter marks in CS: "))
    x = x + [phy] + [che] + [math] + [eng] + [cs]
    dict0[name] = x
for key in dict0:
    if sum_of_elements(dict0[key]) < 200:
        print(key,"has failed")
    else:
        print(key,"has passed")