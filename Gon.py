a = [1, 2, 3, 4, 5, 6]
print(a)
b = []
for i in range(len(a)):
    c = []
    c.append(a[i])
    b.append(c)
print(b)
print(b[0][0])
print(b[1][0])
print(b[2][0])
