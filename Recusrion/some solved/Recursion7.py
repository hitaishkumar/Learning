''' Check palindrome'''
b = [2 , 5 ,8 ,5 , 2,5]

def checkpali(a:list, l , r):
    if l >= r:
        print(a[l] , " ----" , a[r])
        return True
    if a[l] == a[r]:
        return checkpali(a, l+1, r-1)
    else:
        print(a[l] , " ----" , a[r])
        return False
print(checkpali(b , 0 , len(b)-1))