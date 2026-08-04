#I traversed both arrays simultaneously. At each hour, I updated the current number of guests by adding the entries and subtracting the exits.
#After updating the current count, I compared it with the maximum guests seen so far. 
#If the current count was greater, I updated the maximum. Finally, I printed the maximum number of guests present at any point during the part

T = int(input())
E = []
L = []
for i in range(T):
  E.append(int(input()))
for j in range(T):
  L.append(int(input()))
current_guest = 0
max_guest = 0
for i in range(T):
  current_guest = current_guest + E[i] - L[i]
  if current_guest > max_guest:
    max_guest = current_guest
print(max_guest)
