dict0 = {}
for i in range(5):
    name = input("Enter the name: ")
    marks = float(input("Enter the marks: "))
    dict0[name] = marks
def get_key(val):
    for key in dict0:
        if dict0[key] == val:
            return key
    return "key not found"
x = list(dict0.values())
print("Max marks are scored by: ",get_key(max(x)))