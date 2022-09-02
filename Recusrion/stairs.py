'''Climbing stairs leetCode 70'''
'''You are at Top, : 5  climb down to 0, with choices  1 , 2 , 3
Recursive way'''
def sp(n:int , path:str,):
    if n < 0:
        return
    if n == 0:
        print(path)
        return 
    
    sp(n-1, path + "--->1")
    sp(n-2, path + "--->2")
    sp(n-3, path + "--->3")
    
sp(5,"start")
    