def createarray(len: int , starting:int , finish:int) -> list:
    import random
    arr= []
    for i in range(len):
        arr.append(random.randint(starting,finish))
    return arr
def binary_search(a: list,strt_indx:int,last_indx:int,target) -> int :
    '''
    1. sorts input arr
    2. Binary serach
    3. return index of target num
    4. if not found return -1
    5. added strt and last index , to search within list
    '''
    a.sort()
    print(f"{a} --> sorted input array")
    l,r = strt_indx,last_indx
    
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

def pav():
    '''Print All Variables in this .py file'''
    all_variables = dir()
  
    # Iterate over the whole list where dir( )
    # is stored.
    for name in all_variables:
    
    # Print the item if it doesn't start with '__'
        if not name.startswith('__'):
            myvalue = eval(name)
            print(name, "is", type(myvalue), "and is equal to ", myvalue)


def iseven(a) -> bool:
    a = int(a)
    if a % 2 == 0:
        return True
    return False