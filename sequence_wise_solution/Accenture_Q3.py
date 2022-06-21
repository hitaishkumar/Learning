'''
Givena an integer array move all zeroes
to the end of array
keeping the relative order of non zero elements same
'''

a = [1,2,0,0,0,3,4]
def move_0_toleft(a: list) -> list:
    l , r = 0 , 0

    while r <= len(a) - 1 and l <= len(a) - 1 :
        while a[l] != 0 and l < len(a) - 1:
            l+=1
            r+=1
        while a[r] == 0 and r < len(a) - 1:
            r+=1
        a[l] , a[r] = a[r] , a[l]
        l += 1
        r += 1
    return(a)
print(move_0_toleft(a))
        
        
        