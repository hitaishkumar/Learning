a  = [1,2,3,4,5,6,7,8,9,10,798,41,235,124,56,8,65,1,36]

def recurMax(array,idx):
    
    if idx == len(array) - 1:
        return array[idx]
    maxInSmallerArray =  recurMax(array,idx + 1)
    if array[idx] > maxInSmallerArray:
        ans = array[idx]
    else:
        ans = maxInSmallerArray
    
    return ans
    
print(recurMax(a,0))
    