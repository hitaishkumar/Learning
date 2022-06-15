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
maxii = max(idxr,idxc)
ap = []
for i in range(1,maxii+1):
    ap.append(i*2) 
# print(ap)
corner_element = sum(ap)+1
print(corner_element ,"--->", " corner element")

if (idxc % 2 != 0):
    result = corner_element +(idxr-idxc)
else:
    result = corner_element + (idxc - idxr)
print(result ,"--->", " prev result")

# more concise and easy to read version
def rowcol(row:int,col : int):
    ''' read elemnt in zig zig filled 2D matrix
        given the row and column
    '''
    maxi = max(row,col)
    corner = (maxi**2) - maxi +1
    if maxi % 2==0:
        res = corner - (maxi - row)
    else:
        res = corner + (maxi - row)
    return res 
print(rowcol(4,4))