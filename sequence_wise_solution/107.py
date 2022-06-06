'''
Given an unsorted array Arr of size N of positive integers.
One number 'A' from set {1, 2, …N} is missing
and one number 'B' occurs twice in array. 
Find these two numbers.
'''
num = int(input(" enter no of elements in array"))
a = list(int(input(f"enter element indx {i} = 5")) for i in range (num) )
# a = [1, 3, 3,4,5,6,7]

set = set(a)

repeat = sum(a) - sum(set)

ap = []
for i in range(len(a)):
    ap.append(i+1)
missing = sum(ap) - sum(a) + repeat

print(f'''In {a} 
the missing num is : {missing} 
the repeated num is: {repeat}'''
)