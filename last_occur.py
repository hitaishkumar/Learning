arr = [ 1, 3, 5, 5, 5, 5, 67, 123, 125]
def find(arr,n,x) -> list:
    i = []
    for j in range(n):
        if arr[j] == x:
            i.append(j)
    return [min(i), max(i)]
        
       
    
        
print(find(arr,9,5))