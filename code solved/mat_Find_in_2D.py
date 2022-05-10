matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
a = 60
c = len(matrix[0])  # 4 
# print(c)
v = False

for i in range(len(matrix)):
    if i+1 <= len(matrix)-1: # < 2
        if a > matrix[i][c-1] and a <= matrix[i+1][c-1]:
            # scans from 7 to 20  then 20 to 60
            if a in matrix[i+1]:
                v = True
    elif a in matrix[0]:
        v = True
        
print(v)