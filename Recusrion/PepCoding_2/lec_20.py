'''Return all index of an data in an array'''
a = [1,2,3,4,5,6,7,8,3,9,10,11,3]



def findall(arr,idx,data): # return all index of an data in an array
    if idx == len(arr):return idx
    if arr[idx] == data:
        print(idx)
    findall(arr,idx+1,data)
# findall(a,0,3)

def findfirst(arr,idx,data): # return thr first index of the data in the array
    if idx == len(arr):return -1
    if arr[idx] == data:
        return idx
    else:
        return findfirst(arr,idx+1,data)
    
print(findfirst(a,0,3))
    