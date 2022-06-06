'''
Given input of Row and column
find out the element at[row,column] in the 2D matrix 
The matrix is filled in a Zig Zag manner
matrix = [1  2  9  10 25]
         [4  3  8  11 24]
         [5  6  7  12 23]
         [16 15 14 13 22]
         [17 18 19 20 21]
'''

r,c = input(" forst enter row then column").split()
idxr = int(r)-1
idxc = int(c)-1
max = max(idxr,idxc)
ap = []
for i in range(1,max+1):
    ap.append(i*2) 

corner_element = sum(ap)+1
print(corner_element)

if (idxc % 2 != 0):
    result = corner_element +(idxr-idxc)
else:
    result = corner_element + (idxc - idxr)
print(result)
    