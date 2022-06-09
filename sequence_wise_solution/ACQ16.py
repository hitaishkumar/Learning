def intoandsum(into:int):
    sum = 0
    for i in range(1,11):

        print(f" {into} X {i} = {into*i} ")
        sum += (into*i)
    print (f"{sum}") 
    
intoandsum(12)