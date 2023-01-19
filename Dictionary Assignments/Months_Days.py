dict1 = {}
Yeardict = {"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}
month_name = input("Enter the name of the month: ")
print("The number of days are:",Yeardict[month_name])
for i in Yeardict:
    if Yeardict[i] == 31:
        dict1[i] = 31
print(dict1.keys())
x = list(Yeardict.keys())
x.sort()
print(x)