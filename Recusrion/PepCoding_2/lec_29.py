def getstairpath(n:int):
    if n == 0:
        return [""]
    if n < 0:
        return []
    
    fisrt  = ["1"+i for i in getstairpath(n-1)]
    second = ["2"+i for i in getstairpath(n-2)]
    third  = ["3"+i for i in getstairpath(n-3)]
    
    ans = []
    ans.extend(fisrt)
    ans.extend(second)
    ans.extend(third)
    return ans
    
print(getstairpath(5))