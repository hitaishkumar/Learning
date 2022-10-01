def zigzag(n:int):
    '''Under stoop the Euler tree method of ThinkingTree'''
    if n == 0: return
    
    print(f"Pre Order of Euler Tree ----> {n}")
    zigzag(n-1)
    print(f"IN Order of Euler Tree ----> {n}")
    zigzag(n-1)
    print(f"Post Order of Euler Tree ----> {n}")
    # print(f"Pre Order of Euler Tree ---->{n} and {zigzag(n-1)} In Order of Euler Tree ---->{n} {zigzag(n-1)}Post Order of Euler Tree ---->{n}")
zigzag(3)