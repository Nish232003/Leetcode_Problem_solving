#Approach
#Read all balloon colors into an array.
#Use a dictionary (hash map) to count the frequency of each color.
#Traverse the original array again and print the first color whose frequency is odd.
#If no odd-frequency color exists, print "All are even".

n = int(input())
b = []
f = {}
for _ in range(n):
  ch = input().strip()
  b.append(ch)
  f[ch] = f.get(ch,0) + 1
found = false
for ch in b:
  if f[ch] % 2 != 0:
    print(ch)
    found = True
    break
if not found:
  print("All are even")
