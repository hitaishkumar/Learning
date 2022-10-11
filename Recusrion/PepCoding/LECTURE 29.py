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
    
    
    ans = []
    for i in a:
        ans.append(i + "1")
    for i in b:
        ans.append(i + "2")
    for i in c:
        ans.append(i + "3")
    # ans.extend(a)
    # ans.extend(b)
    # ans.extend(c)
    
    return ans
print(getstairpath(4))