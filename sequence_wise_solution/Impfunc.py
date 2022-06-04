def createarray(len: int , starting:int , finish:int) -> list:
    import random
    arr= []
    for i in range(len):
        arr.append(random.randint(starting,finish))
    return arr
def binary_search(a: list,t) -> int :
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
        if t > a[m]:
            l = m+1
        elif t < a[m]:
            r = m-1
        else:
            # print(m)
            return m