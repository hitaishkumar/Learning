def createarray(len: int = 20 , starting:int = 1 , finish:int = 10) -> list:
    import random
    arr= []
    for i in range(len):
        arr.append(random.randint(starting,finish))
    return arr
def binary_search(a: list,target) -> int :
    '''
    1. sorts input arr
    2. Binary serach
    3. return index of target num
    4. if not found return -1
    '''
    a.sort()
    print(f"{a} --> sorted input array")
    l,r = 0,len(a)
    
    while l<=r:
        m = (l+r)//2
        if target > a[m]:
            l = m+1
        elif target < a[m]:
            r = m-1
        else:
            # print(m)
            return m
def ispalindrome(a) -> bool:
    '''Reverse a string -> a[::-1] 
       compare with original'''
    a = str(a)
    return a == a[::-1] 
def revarray(a:list , start:int ,end: int) -> list:
    ''' reverses a array recursively'''
    if(start < end):
        a[start] , a[end] = a[end], a[start]
        # print(a)
        revarray(a,start + 1 , end -1)
    return a

def iseven(a) -> bool:
    a = int(a)
    if a % 2 == 0:
        return True
    return False