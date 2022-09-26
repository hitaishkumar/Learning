def letterCombinations( digits: str) -> list[str]:
    dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    res = []
    
    def bt(idx,currstr):
        if len(currstr) == len(digits):
            res.append(currstr)
            return
        for c in dic[digits[idx]]:
            bt(idx+1 , currstr+c)
            
    if digits:
        bt(0,"")
    return res

print(letterCombinations("23"))