a =[20, 15, 26, 2, 98, 6]
c = a
print(c)
c.sort()
print(c)
for i in range(6):
    for j in range(6):
        if c[j] == a[i]:
            print(j)
