'''Get Key-Pad Combination for a given Number'''

hashTable = ["", "", "abc", "def", "ghi", "jkl",
             "mno", "pqrs", "tuv", "wxyz"]

def getKeypadCombo(a):
    if len(str(a)) == 0:
        return [""]
    
    
    a =list(str(a))
    first = a.pop(0)
    restCombo = getKeypadCombo("".join(a))
    ans = []
    
    for i in hashTable[int(first)+1]:
        for j in restCombo:
            ans.append(i+j)
    return ans
[print(str(i)) for i in getKeypadCombo(666)]