# Minimum no. of Jumps to reach end of an array
# https://youtu.be/dJ7sWiOoK7g
import random
ra= []
for i in range(6):
   ra.append(random.randint(1,10)) 
print(ra)
print(len(ra))

def jump(ra:list) -> bool:
    l=r = 0
    res = 0
    
    while(r < len(ra) -1):
        farthest = 0
        for i in range(l,r+1):
            farthest = max(farthest,i+ra[i])
        l = r + 1
        r = farthest
        res += 1
    
    return res

print(jump(ra))            