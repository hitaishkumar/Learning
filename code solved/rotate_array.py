from operator import le


# a = [1, 4, 8, 10, 3,4,5,6,8,9,4,2,1,3]
# b = [1, 4, 8, 10, 3,4,5,6,8,9,4,2,1,3]
def Rotateclockwise(a: list) -> list:
    b = a
    for i in range(len(a)):
        if i == 0:
            b[i] = a[len(a)-1]  
        else:
            b[i] = a[i-1]
    return b
      