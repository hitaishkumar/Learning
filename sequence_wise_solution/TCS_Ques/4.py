# Count frequency of each element in the array
import Impfunc as imp

a= imp.createarray(20,2,15)
b={}

print(a)
for a in a:
    if b.get(a,0) == 0:
        b[a] = 1
    else:
        b[a] += 1
print(b)

# using python built in modules
from collections import Counter
c = "jahfsjhdfsjkdfkjsfsddhhsbsjhvbsjhvbshvbjfbvsfvf"
print(Counter(c))
