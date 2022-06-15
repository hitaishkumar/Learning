# Rearrange array in increasing-decreasing order
import Impfunc as imp
a = imp.createarray(20,1,50)

def revsort(a:list , start:int , end:int):
    b = a[start:end+1]
    b.sort(reverse=True)
    return b
print(revsort(a,0,len(a)-1))