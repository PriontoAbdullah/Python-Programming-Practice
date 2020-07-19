#list inside list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for sublist in matrix:
  for i in sublist:
    print(i)
print(type(matrix))
print(matrix[1][1]) #5