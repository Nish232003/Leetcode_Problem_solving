#I traversed each row of the matrix and counted the number of occupied parking spaces (1) in that row.
#While traversing, I maintained the maximum count of occupied spaces seen so far and stored the corresponding row index. 
#After checking all rows, I returned the row number having the maximum number of occupied parking spaces."

R = int(input())
C = int(input())
M = []
for i in range(R):
  row = []
  for j in range(C):
    row.append(int(input()))
  M.append(row)
max_count = 0
answer = 1
for i in range(R):
  count = M[i].count(1)
  if current > max.count:
    max.count = current
    answer = i+1
print(answer)
    
