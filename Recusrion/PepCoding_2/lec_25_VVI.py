'''Get subsequence of a string : 2^n'''

def GetSubsequence(s):
    
    if len(s) == 0:
        return [""]
    
    s = list(s)
    first= s.pop(0)
    subseq = GetSubsequence(s)
    ans = []
    for i in subseq:
        ans.append(""+str(i))
        ans.append(str(first) + str(i))
    return ans
print(GetSubsequence("abccd"))