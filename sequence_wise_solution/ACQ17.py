#  Write a program in C such that it takes a lower limit and upper limit as inputs and print all the intermediate palindrome numbers.
import Impfunc as imp
def findpal(low:int, up:int) -> int:
    for i in range(low,up+1):
        if imp.ispalindrome(i):
            print(i)
            
findpal(2,1000)