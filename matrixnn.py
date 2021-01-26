X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for a in range(len(X)):
   for b in range(len(X[0])):
       result[a][b] = X[a][b] + Y[a][b]

for i in result:
  print(i)
