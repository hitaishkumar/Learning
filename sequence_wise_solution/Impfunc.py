def createarray(len: int , starting:int , finish:int) -> list:
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


def iseven(a) -> bool:
    ''' takes any convert to int'''
    a = int(a)
    if a % 2 == 0:
        return True
    return False

def isprime(a) -> bool:
    ''' takes any convert to int'''
    a = int(a)
    for i in range(2,a):
        if a % i == 0:
            return False
    return True
# https://www.youtube.com/watch?v=R_wDA-PmGE4&ab_channel=FelixTechTips ---> INSERTION SORT
def insertionsort(arr:list) -> list:
    ''' input : list  output : list'''
    leng = len(arr)
    for i in range(1, leng):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1] , arr[j] = arr[j] , arr[j-1]
            # print(f" here {a[j-1]} is swapped with {a[j]} and the array is{arr} ")
            j -= 1
    return arr

# a = createarray(5,1,100)
# print(a)
# print(insertionsort(a))
