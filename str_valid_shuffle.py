a = "1XY22"
b = "Y1X2"

for i in a:
    if len(a) == len(b):
        if i in b:
            print(f"{a} is a valid shuffel of {b} ")
        else:
            print(f"{a} is not in {b} ")
    else:
        print(f"{a} is not in {b} ")
        