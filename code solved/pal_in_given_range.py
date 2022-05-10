def ispalindrome(gr: int):
    l = [str(a) for a in str(gr)]  # number to list of integers
    # print(l)
    l.reverse()
    # print(int("".join(rl)))
    rn = int("".join(l))
    if gr ==rn :
        return True
    else:
        return False

# now for a given range:

a = int(input(" range upto where palindromes are needed  :  "))
for i in range(a):
    if (ispalindrome(i)):
        print(i)

