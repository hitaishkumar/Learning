a= "abcasfhajfhsaassjfhsdjfhsdfsf"
## print out this a5b1c1d2f6h4j3s7
# sorted alphabet with thier frequency

def usingcollections():
    from collections import Counter
    cc = Counter(a)
    a = [i for i in sorted(cc)] # sort dict by key value
    res = ""
    for i in a:
        res += i + str(cc[i])
    print(res)


def usinglists():
        
    ans = []
    b = set(a)
    for i in b:
        ans.append(i)
        count = a.count(i)
        ans.append(str(count))
    print(ans)
    print("".join(ans) , " ------> join method ")


def iterablemethod():
    b =list(a)
    b.sort()
    count = 0
    res = ""
    for i in range(len(b)):
        if i+1 < len(b) -1 :
            if b[i] == b[i+1]:
                count += 1
            else:
                res = res + str(b[i]) + str(count + 1)
                count = 0
    print(res)
            
    

