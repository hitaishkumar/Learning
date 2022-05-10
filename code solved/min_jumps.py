

arr= [1, 5, 5, 8, 9, 2, 6, 7, 6, 8, 9]
jmp = 0
rmlen = len(arr)-1
elm = 0
count = 0
while elm < rmlen:
    rmlen -= elm
    # elm = arr[jmp]
    elm = arr[elm]
    count += 1
    
print(count)  
    