from itertools import count


a = "aaaaaaaaabasss"
b = "aba"
length = len(a) - len(b)
count = 0
pos = 0
for i in range(length):
    if b in a[i:i+len(b)]: count +=1
print(count)