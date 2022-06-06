def ispalindrome(a:str) -> bool:
    '''Reverse a string -> a[::-1] 
       compare with original'''
    
    return a == a[::-1] 


print(ispalindrome("cuttuc"))    
    
    