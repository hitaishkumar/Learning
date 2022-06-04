# https://www.youtube.com/watch?v=4sQL7R5ySUU&t=2s&ab_channel=NeetCode

# First and Last Position of Element in Sorted Array - Binary Search 

import Impfunc as im

a = im.createarray(12,2,15)
a.sort()

def solution(arr: list , target:int):
    left = binary_search(arr,target,True)
    right = binary_search(arr,target,False)
    return [left,right]

def binary_search(a: list,t,leftbias: bool):
    
    # print(f"{a} --> before sorted")
    # a.sort()
    # print(a)
    l,r = 0,len(a)
    i = -1
    while l<=r:
        m = (l+r)//2
        
        if t > a[m]:
            l = m+1
        elif t < a[m]:
            r = m-1
        else:
            i = m
            if leftbias:
                r = m -1
            else:
                l = m + 1 
        return i
a.sort()
print(a)
print(solution(a,5))
# print(k)
        








