# https://takeuforward.org/data-structure/reverse-a-given-array/



a = "yaallahbitch"
b = list(a)

def revarray(a:list , start:int ,end: int) -> int:
    
    if(start < end):
        a[start] , a[end] = a[end], a[start]
        # print(a)
        revarray(a,start + 1 , end -1)
   
revarray(b, 0 , len(b)-1)        
print(b)

