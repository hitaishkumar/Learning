'''Finad all indices of a values in a array'''

a = [1,2,3,4,5,5,5,5,5,6,7,8,9,10,11,9,9]

def findallindices(arr,idx,data,foundsofar):
    if len(arr) == 0:
        return 0
    
    if arr.pop(0) == data:
        foundsofar += 1
        print(idx)
    foundfurther = findallindices(arr,idx+1,data,foundsofar)
    
    return max(foundfurther,foundsofar)
# print(findallindices(a,0,5,0))


def fai(arr,idx,data,fsf): 
    # count how many variables while going up in recursion
    # return that length of array , 
    # and subtiute idx at returned array[fsf] while returning in recursion
    if idx == len(arr):
        return [0] * fsf
    
    if arr[idx] == data:
        ans = fai(arr,idx+1,data,fsf + 1)
        ans[fsf] = idx
        return ans
    else:
        ans = fai(arr,idx+1,data,fsf)
        return ans
print(fai(a,0,9,0))