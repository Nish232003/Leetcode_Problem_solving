#I traversed the array only once while maintaining the maximum element seen so far (max_so_far). 
#Since the first element has no previous elements, I counted it by default. For every subsequent element, I checked whether it was greater than max_so_far. 
#If it was, I incremented the count and updated max_so_far. 
#This ensures each element is compared only with the maximum of all previous elements instead of checking every previous element individually.

n= int(input())
arr = []
for _ in range(n):
  arr.append(int(input()))
count = 1
max_so_far = arr[0]
for i in range(1,n):
  if arr[i] > max_so_far:
    count += 1
    max_so_far = arr[i]
print(count)
