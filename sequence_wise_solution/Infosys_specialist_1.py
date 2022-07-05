''''Today you decided to go to the gym. You currently have energy equal to E units. There are N exercises in
the gym. Each of these exercises drains Ai amount of energy from your body.
You feel tired if your energy reaches 0 or below. Calculate the minimum number of exercises you have
to perform such that you become tired. Every unique exercise can only be performed at most 2 times as
others also have to use the machines.
If performing all the exercises does not make you feel tired, return -1.'''

'''

E :: INTEGER
The first line contains an integer, E, denoting the Energy.
E :: 1 -> 10^5
N :: INTEGER
The next line contains an integer, N, denoting the number of exercises.
N :: 1 -> 10^5
A :: INTEGER ARRAY
Each line i of the N subsequent lines (where 0 ≤ i < N) contains an integer describing the amount of
energy drained by i-th exercise.
A[i] :: 1 -> 10^5

'''
e = 6
a = [1,2,3]
a.sort()
for i in reversed(a):
    if i == e:
        print(f" do {i} once")
        break
    if i * 2 == e:
        print(f" do {i} 2 times")
        break

b = []
ssum = 0
for i in a:
    b.append(i)
    b.append(i)
b.sort()
# print(b , " ----- printing b")
start = len(b) -1
end = len(b) -1
# print(sum(b[start:end+1]) , " sum of b whole")

while True:
  
    ssum = sum(b[start:end+1])
    # print(ssum, " ------printing SSum")
    if ssum == e:
        print(len(b[start:end+1]) , " --printing the count of excercise")
        break
    if start == 0:
        print("-1" , " ----------start == 0 ")
        break
    if ssum < e:
        start -= 1
    if ssum > e:
        end -= 1 
    












       
        
   
