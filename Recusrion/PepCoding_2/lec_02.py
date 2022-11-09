'''print 1 to n'''
# whatever you do after call the function is executed while returning back from base case:

def p_one_to(a:int):
    if a == 0:
        return 
    p_one_to(a-1)
    print(a)
p_one_to(5)