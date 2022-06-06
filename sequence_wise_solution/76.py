'''
Given a string S consisting of only opening and closing curly brackets '{' and '}',
find out the minimum number of reversals required
to convert the string into a balanced expression.
A reversal means changing '{' to '}' or vice-versa.
'''
s = "}{{}}{{"
def balancenum(a:str) -> int:
    close = 0
    open = 0
    if len(s) % 2 == 0:
        # print("yes")
        for a in s:
            if a == "{":
                open += 1
            else:
                if open == 0:
                    close += 1
                else:
                    open -= 1
        res = ((open + close) // 2) +1
        return res
                        