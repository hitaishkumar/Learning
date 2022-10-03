'''Last Index of Occurrence - Question | Recursion | Data Structures and Algorithms in JAVA
'''
'Very Very Important'
    
a = [8,4,5,6,4]

def lastidx(arr,idx,data):
    if idx == len(arr):
        return -1
    
    liisa = lastidx(arr,idx +1 ,data)
    
    if liisa == -1 :
        if arr[idx] == data:
            return idx
        else:
            return -1
    else:
        return liisa    
        
        
    
print(lastidx(a,0,4))