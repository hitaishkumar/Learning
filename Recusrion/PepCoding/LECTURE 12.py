'''TOWER of Hanoi's algorithm'''
def toh(stack_number , tower1, tower2, tower3):
    '''here the sequence of tower is that of SOURCE -> DESTINATION -> Using HELPER'''
    if stack_number== 0:
        return
    toh(stack_number-1 , tower1, tower3 , tower2)
    print(f"move from {tower1} to {tower2}")
    toh(stack_number-1 , tower3 ,tower2,tower1)

toh(3, 1,2,3)