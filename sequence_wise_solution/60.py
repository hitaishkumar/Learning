#  https://www.youtube.com/watch?v=5e63aHK6Q-E&t=183s&ab_channel=TECHDOSE

# Find if one string is a rotation of another string

def findrot(a, c) -> bool:
    if len(a) == len(b):
        for i in range(len(a)):
            b = ""  
            d = a[i+1:]
            e = a[0:i+1]
            b = d + e
            # print(b) if want to see the shuffle
            if c == b:
                return True
        
    return False
    
# Basic method of checking with O(n^2)
print(findrot("abcd","dabc"))


# usage of KMP algorithm