inputnum = int(input("Enter an octal number"))
octnum = oct(inputnum)
def conversion(num):
    decnum = int(num,8)
    binnum = bin(decnum)
    hexnum = hex(decnum)
    return binnum,hexnum,decnum
print(conversion(octnum))