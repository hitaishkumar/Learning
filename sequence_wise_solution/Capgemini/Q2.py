'''Find if prime'''
a =4500

def new_func(a):
    for i in range(2,a):
        if a%i == 0:
            break
        # print('not prime')
        else:
            return True
    return False
print(new_func(123456798))
        