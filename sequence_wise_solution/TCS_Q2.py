question = '''
Bastin once had trouble finding the numbers in a string.
The numbers are distributed in a string across various test cases.
There are various numbers in each test case you need to find the number in each test case.
Each test case has various numbers in sequence.
You need to find only those numbers which do not contain 9. 
For eg, if the string contains “hello this is alpha 5051 and 9475”.
You will extract 5051 and not 9475.
You need only those numbers which are consecutive and you need to help him find the numbers.
Print the largest number.
Note: Use long long for storing the numbers from the string.
Input Format :
The first line consists of T test cases and next T lines contain a string.
Output Format:
For each string output the number stored in that string if various numbers are there print the largest one. 
If a string has no numbers print -1.
'''


a = "hello this is alpha 5051 and 9475"
b = a.split(" ")
ans = []
print(b)
for i in b :
    if "9" in i:
        ans.append(i)
        print(ans)
    else:
        print(-1)   