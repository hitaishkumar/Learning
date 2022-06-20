'''
Doug is fond of change ,
every now and then he tries to do new things
This time he caught up with a rod comprising of 
negative(N) and positive(P) charge 
. He is asked to calculate the
maximum net electrostatic field 
possible in region due to the rod.

'''


c = [4,3,5]
s = ['P' , 'N' ,'P']
# print(len(c) , len(s))
sum = 0
for i in range(len(s)):
    if s[i] == 'P':
        sum += c[i]*100
    else:
        sum -= c[i]*100
print(sum)