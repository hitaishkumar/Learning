def printnum(a:int):
    if a == 0:
        return
    print(a)
    printnum(a-1)
printnum(4)
print("--------------------------------")

def printnumTillMax(a:int , max:int ):
    if a > max :
        return
    print(a)
    printnumTillMax(a+1,max)
    
printnumTillMax(4,10)