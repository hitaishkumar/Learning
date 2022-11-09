'''print decreasing increasing'''

def p_decreasing_increasing(a:int):
    if a == 0:
        return
    print(a)
    p_decreasing_increasing(a-1)
    print(a)
p_decreasing_increasing(6)
# 6-> 1 then  1->6

'''print increasing decreasing'''

def p_increasing_decreasing(a:int, max:int):
    if a == max+1:
        return
    print(a)
    p_decreasing_increasing(a+1,max)
    print(a)
p_decreasing_increasing(1,10)
# 1 -> max then  max -> 1