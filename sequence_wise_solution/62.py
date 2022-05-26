# a = "112234444"
from timeit import repeat


def say(a):
    count  = 0
    b = ""
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            count += 1
        else:
            count += 1
            b = "".join([b,str(count),a[i]])
        
            count = 0
    count = 0
    for i in reversed(range(len(a))):
        if a[i] == a[i-1]:
            count += 1
        else:
            count += 1
            # print( a[i], "  " , count)
            b = "".join([b,str(count),a[i]])
        
            break
        
    return b
# print(say("21"))



def saylevel(n:int):
    if n == 1:
        return "11"
    if n == 2:
        return "21"
    if n >= 3:
        a = "21"
        for i in range(n-2):
            a = say(a)
            a = str(a)
    return str(a)

# print(saylevel(5))



##  write to a file 
f = open('Count_and_say_output.txt', 'w')
for i in range(1,20):
    value = repr(saylevel(i))
    f.write(" value "+ str(i)+ "=" + value + "\n")   
f.close()  # you can omit in most cases as the destructor will call it