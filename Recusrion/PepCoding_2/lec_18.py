'''FInad max of an array'''
a = [1,2,3,4,5,56,7,8,9,10,11]
def findmax(arr:list,idx):
    if idx == len(arr): return arr[idx-1]
    maxo = findmax(arr,idx+1)
    return max(arr[idx],maxo)
print(findmax(a,0))
