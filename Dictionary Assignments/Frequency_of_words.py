dict0 = {}
line = input("Enter the text: ")
x = line.split()
word_freq = 0
for i in x:
    word_freq = x.count(i)
    dict0[i] = word_freq
print(dict0)