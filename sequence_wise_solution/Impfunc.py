def createarray(len: int , starting:int , finish:int) -> list:
    import random
    arr= []
    for i in range(len):
        arr.append(random.randint(starting,finish))
    return arr