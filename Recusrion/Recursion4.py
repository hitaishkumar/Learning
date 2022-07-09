'''sum of array'''
import random
a =[]
for i in range(10):
    a.append(random.randint(2 , 100))
print(a ,  " --------> Generated array ")
print(sum(a), " ------> Correct ans")

def arrsum(a):
    if len(a) == 1:
        return a[0]

    return a[0] + arrsum(a[1:])

print(arrsum(a), " ------> is the calculated ans")