'''print array in reverse using recursion'''

a = [1,2,3,4,5,6,7,8,9]

def displayreverse(array,idx):
    if idx == len(array):
        
        return 
    displayreverse(array,idx + 1)
    print(array[idx])
#  Recursive call ke bad wala Code stack se niche ate time run hota hai
#  Recursive call ke pehle wala Code stack me Upar jate time run hota hai
displayreverse(a,0)