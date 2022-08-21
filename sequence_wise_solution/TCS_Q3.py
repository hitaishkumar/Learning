# a = input()

'''
Given Two binary numbers ( in O and 1 ) in the form of string. Find out whether there
is a possibility whether these numbers can become equal by rearranging their
respective Os and Is.
For ex : 101 and 011 can be arranged within themselves to become either 101 or 011.

'''

a = "101000101"
b = "101000101"

print(a.count("0") , "ishjdf" , b.count("0"))

if a.count("0") == b.count("0") and a.count("1") == b.count("1"):
    print("True")

 