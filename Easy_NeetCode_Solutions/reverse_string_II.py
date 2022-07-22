# https://www.youtube.com/watch?v=_d0T_2Lk2qA&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=57&ab_channel=NeetCode

''' reverse a array using stack'''

a = "hello"
stack = []

for a in a:
    stack.append(a)
print(stack)
ans = []
for i in range(len(stack)-1, -1 ,-  1):
    ans.append(stack[i])
print(ans)