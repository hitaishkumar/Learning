'''display array using recursion'''

a = [1,2,3,4,5,6,7,8,9]

def displayarray(array, idx):
    
    
    if idx == len(array):
        return
    print(array[idx])
    displayarray(array, idx + 1)
displayarray(a,0)