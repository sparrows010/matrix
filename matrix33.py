X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]


for a in range(len(X)):
   for b in range(len(Y[0])):
       for c in range(len(Y)):
           result[a][b] += X[a][c] * Y[c][b]

for i in result:
   print(i)
