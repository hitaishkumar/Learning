''' Fibonacci sequence array'''



def getfibonacci(index:int):
    if index <= 1: # applicable because index == element at  index 0 ,1
        return index 
    return getfibonacci(index - 1) + getfibonacci(index - 2)

a = [ getfibonacci(index) for index in range(10)]
print(a)