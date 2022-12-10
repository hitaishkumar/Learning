'''display a array'''

a = [1,2,3,4,5,6,7,8,9,10,11]

def disparr(arr:list,n):
    if n == len(arr):return
    
    print(arr[n])
    disparr(arr,n+1)
disparr(a,0)
    