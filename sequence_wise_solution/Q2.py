# Merge sort Implemented

from operator import index, le


def CreateArray(size = 20, max = 100): # Create a Random array of size 20
    from random import randint
    return [randint(0,max) for _ in range(size)]


def Merge(a,b):
    c = [] # output array
    
    aindx , bindx = 0,0
    while aindx < len(a) and bindx < len(b):
        if a[aindx] < b[bindx]:
            c.append(a[aindx]) 
            aindx += 1
        else:
            c.append(b[bindx])
            bindx += 1
    if aindx ==len(a): c.extend(b[bindx:])
    else: c.extend(b[bindx:])