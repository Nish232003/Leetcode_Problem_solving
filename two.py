#Counting frequency problem
#The problem asks us to determine the difference between the number of '*' and '#' characters.
#I traversed the string once and maintained two counters: one for '*' and one for '#'. After counting both, I computed star - hash. 
#If the result is positive, it means there are more '*'; if it's negative, there are more '#'; and if it's zero, both counts are equal, so the string is already valid.

s = input()
star = 0
hash = 0
for ch in s:
  if ch == '*':
    star += 1
  elif ch == '#':
    hash += 1
print(star-hash)
