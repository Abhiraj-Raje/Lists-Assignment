s1 = input("Enter first string: ")
s2 = input("Enter first string: ")
def lengthcheck(a,b):
    if len(a) == len(b):
        return True
    else:
        return False
print(lengthcheck(s1,s2))
