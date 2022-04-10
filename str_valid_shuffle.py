a = "XY32"
b = "Y1X2"
def shuffle(a,b):
    counter = 0
    for i in a:
        if len(a) == len(b):
            if i not in b:
                counter += 1
        else:
            # print(f"{a} is not in {b} ")
            return False
    if counter >= 1:
        return False
    else:
        return True
print(shuffle("xi33","3ixx"))
            