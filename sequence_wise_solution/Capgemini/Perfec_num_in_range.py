def ppn(start, end):
    '''return arr of perfect num in a given range'''
    ans = []
    
    for i in range(start, end):
        s = 0
        for j in range(1,i):
            
            if i%j == 0:
                s += j
        if s == i:
            ans.append(s)
          
    return(ans)
print(ppn(1, 500))      