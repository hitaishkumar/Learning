# https://prepinsta.com/accenture/coding/
'''
An Autobiographical Number is a number N such that the first digit of N represents the count of how many zeroes are there in N,
the second digit represents the count of how many ones are there in N and so on.

You are given a function, def FindAutoCount(n):

The function accepts string “n” which is a number and checks whether the number is an autobiographical number or not.
If it is, an integer is returned, i.e. the count of distinct numbers in ‘n’. If not, it returns 0.


Input:

n: “1210”

Output:

3

Explanation:

0th position in the input contains the number of 0 present in input, i.e. 1, 
in 1st position the count of number of 1s in input i.e. 2, 
in 2nd position the count of 2s in input i.e. 1, and 
in 3rd position the count of 3s i.e. 0, 
so the number is an autobiographical number.

Now unique numbers in the input are 0, 1, 2, so the count of unique numbers is 3. So 3 is returned.
'''
from itertools import count


n = "1210"
b= set(n)
c= "0123456789"
for i in range(len(n)):
    if n[i] == n.count(c[i]):
        ans = True
    else:
        ans = False
    # print(f" the freq of {i} in {n} is {n.count(i)}")
if ans:
    print(len(b))
else:
    print("0")
def FindAutoCount(n):
    pass