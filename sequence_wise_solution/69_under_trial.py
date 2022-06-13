'''
Given two strings s and t. Return the minimum number of operations required to convert s to t.
The possible operations are permitted:

Insert a character at any position of the string.
Remove any character from the string.
Replace any character from the string with any other character.

'''
s = "ecfbefdcfca"
t = "badfcbebbfaaaa"
ans = 0
dc = 0
final = 0
if len(s) != len(t):
    ans += abs(len(s) - len(t))
a = min(s,t)
for i in range(len(t)):
    if t[i] != s[i] :
        dc += 1
final += dc + ans
print(final)
        
        