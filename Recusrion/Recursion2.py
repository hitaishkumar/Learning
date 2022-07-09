'''max of an array'''
import random
a =[]
for i in range(50):
    a.append(random.randint(2 , 100))
print(a ,  " --------> Generated array ")

def maxarr(a:list , i: int):
    if i == len(a) - 1:
        return a[i]
    cm = a[i]
    rm = maxarr(a,i+1)
    return max(cm , rm)
    
print(maxarr(a, 0))