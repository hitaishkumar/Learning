'''Display an array using recursion'''
import random
a =[]
for i in range(10):
    a.append(random.randint(2 , 100))
print(a ,  " --------> Generated array ")

def printarr(a:list , i:int):
    if i == len(a): 
        return 
    print(a[i])
    printarr(a,i + 1)
    
print(f" {printarr(a , 0)}  -------> uptill here printed straight")

def printrevarr(a: list , idx: int):
    # print(idx)
    if idx == 0: # given index value is  1 based , not 0 based
        return
    print(a[idx-1])
    printrevarr(a, idx - 1)
print(f" {printrevarr(a , 10)}  -------> uptill here printed reverse")  
