## Brute Force

s = "abba"
a = []
for i in s:
    a.append(i)
a.reverse()
b = a
if b is a:
    print("given string is palindrome")
    
## optimized:
def chp(a:str) -> bool:
    j = len(a)
    for i in range(len(a)):
        if a[i] == a[j-1]:
            j -= 1
            # print(i , j)
            if len(a) % 2 == 0:
                if i == j+1:
                    return True
            else:
                if i == j:
                    return True
            
        else:
            return False
            
                
    
        
print(chp("abccvba"))              