def isSubsequence(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False
    
    sp , tp = 0, 0
    
    while tp < len(t) -1 :
        if t[tp] != s[sp]:
            tp += 1
        else:
            sp += 1
            tp += 1
    if t[-1] == s[-1] and sp == len(s) - 1 :
        return True
    else:
        return False
print(isSubsequence( "abc","ahbgdc"))