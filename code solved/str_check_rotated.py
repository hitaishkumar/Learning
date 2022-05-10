
a = "abcd"
b = "bcda"
if len(a) == len(b):
    # for right rotation:
    k = len(a)
    cl = []
    j = list(a)
    for i in range(k):
        j.append(j[0])
        del j[0]  # delete element in a list by index
        c = "".join(j)
        cl.append(c)
    print(f"{b in cl} is a rotation")
else:
    print("not a rotation")