def strStr(haystack: str, needle: str) -> int:
    
    ans = -1
    # print(haystack[0:len(needle)])
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if haystack[i:i+len(needle)] == needle[:]:
                ans = i
                
                return ans
    return ans
strStr("hello","ll")