'''display array in reversed order'''

a = [1,2,3,4,5,6,7,8,9,10,11]

def disparrrev(arr:list,idx):
    if idx < 0: return
    print(arr[idx])
    disparrrev(arr, idx-1) 
    
# disparrrev(a,len(a)-1)


def disp2(arr:list,idx):
    
    if idx == len(arr): return
    
    print(arr[len(arr)-1 - idx])
    
    disp2(arr,idx+1)
    
disp2(a,0)