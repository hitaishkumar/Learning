# https://takeuforward.org/data-structure/remove-duplicates-from-an-unsorted-array/

# hashtable method
from collections import Counter
import Impfunc as im

# a = im.createarray()
a = [8, 7, 3, 9, 4, 10, 7, 2, 5, 5, 5, 10, 5, 5, 2, 4, 6, 3, 6, 7]
print(a)
# c = Counter(a)
# print(c)
b = {}
for i in a:
    if b.get(i,0):
        b[i] += 1
    else:
        b[i] = 1
print(b)
ans = [i for i in b if b[i] == 1]
print(ans)
        