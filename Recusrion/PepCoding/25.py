'''Get Subsequence - Introduction to Arraylists | Recursion | Data Structures and Algorithms in JAVA
'''
def getsubsequence(string):
    
    first = string[:1]
    rest = string[1:]
    if len(first) == 0:
        return [""]
    found_sequence = getsubsequence(rest)
    
    ans = []
    for i in found_sequence:
        ans.append(first + i)
        ans.append(""+ i)
    
    return ans
print(getsubsequence("abc"))
