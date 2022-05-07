r = int(input(" row"))
c = int(input(" column"))

if r < c:
    x = (c-1)*(c-1)
    y = x+r
    print(y)
else:
    x = (r-1)*(r-1)
    y = x+c
    print(y)