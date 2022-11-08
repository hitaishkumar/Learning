def printdec(a:list):
    if len(a) == 0:
        return
    print(a[0])
    printdec(a[1:])
# printdec([1,2,33,43,3,23,393,3])

def print_reverse(a:list):
    if len(a) == 0:
        return
    print(a.pop())
    printdec(a[:-1])
# print_reverse([1,2,33,43,3,23,393,3])
def printdec_num(a:int):
    if a == 0:
        return 
    print(a)
    printdec_num(a-1)
# printdec_num(9)
    