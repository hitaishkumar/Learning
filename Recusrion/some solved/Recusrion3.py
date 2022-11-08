'''
First Index of occurrence '''

# https://www.youtube.com/watch?v=OD39jBFjgdI&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=19&ab_channel=Pepcoding

import random
a =[]
for i in range(10):
    a.append(random.randint(2 , 10))
print(a ,  " --------> Generated array ")

def printindx(a: list , i:int , num:int):
    if i == len(a):
        return
    if a[i] == num:
        return 
    
    printindx(a, i+1 , num)
    return i
    
print(printindx(a, 0 , 5))