a = input()
b = list(a)
print (b)
ans = []
def iseven(a):
    a= int(a)
    if a% 2 == 0:
        return True 
    return False
for e in b:
    if iseven(e):
        ans.append(int(e)+1)
    else:
        ans.append(int(e)-1)
c= "".join(str(ans))       
print(c)