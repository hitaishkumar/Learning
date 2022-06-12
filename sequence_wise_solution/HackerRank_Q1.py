'''
Question
Merge the Tools!

https://www.hackerrank.com/challenges/merge-the-tools/problem
'''

def merge_the_tools(string, k):
    # your code goes here
    prev = [string[i:i+k] for i in range(0,len(string),k)]
    
    for a in prev:
        ans = set(a)
        print("".join(ans))
    # print(prev)