from operator import index
import Impfunc

a = Impfunc.createarray(10, 1, 10)
b = Impfunc.createarray(10, 1, 10)
c = Impfunc.createarray(10, 1, 10)
i, j = 0, 0  # b,c
print(a, b, c)
for a in a:
    if a in b and a in c:
        print(f"{a} is found in {b} and {c} at index {b.index(a)} and {c.index(a)} ")
