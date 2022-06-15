'''
Write a program to find whether an array is a subset of another array or not.

Given arr1[] and arr2[], 
we need to find whether arr1[] is a subset of arr2[]
. An array is called a subset
of another if all of its elements 
are present in the other array.'''

from Impfunc import createarray
# solved using Hash tables 
# O(m + n) TC 
# O(m+n) SC
a =  createarray()
b= createarray(5,7,10)
print(a , "  " , b)

ca = {}
for i in a:
    if ca.get(i,0):
        ca[i] += 1
    else:
        ca[i] = 1
print(ca)
flag = True
for i in b:
    if ca.get(i,0):
        ca[i] -= 1
    else:
        flag = False
        print(f"{b} is not sub of {a}")
        break
if flag:    
    print("b is sub" )
print(ca)