'''Get Stairs Path - Solution | Recursion | Data Structures and Algorithms in JAVA
'''


a = ""
b = "d" + a
print(b)

def getstairpath(num):
    if num < 0:
        return []
    elif num == 0:
        return [""]
    
    a = getstairpath(num-1) 
    b = getstairpath(num-2)
    c = getstairpath(num-3)
    
    
    for i in a:
        i  = '1' + i
    for i in b:
        i  = '2' + i
    for i in c:
        i  = '3' + i
    ans = []
    ans.extend(a)
    ans.extend(b)
    ans.extend(c)
    
    return ans
print(getstairpath(4))