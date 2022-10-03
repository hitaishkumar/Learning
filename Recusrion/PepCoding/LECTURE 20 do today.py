'''First Index of Occurrence in Array using Recursion | Algorithms in JAVA'''

a = [8,4,5,6,4,6,4,8,1,2,31,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8]

def firstindexR(a:list[int], idx,findd) :
    
    if idx == len(a) : return -1
    
    if a[idx] == findd: return idx
    
    return  firstindexR(a,idx + 1,findd) 
    
print(firstindexR(a,0,311))