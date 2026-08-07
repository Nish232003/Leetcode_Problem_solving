#Approach
#Create an empty stack to simulate the text being typed.
#Traverse each character of the input string.
#If the character is a lowercase letter, push it onto the stack.
#If the character is #:
#If the stack is not empty, pop the top element (delete the last typed character).
#If the stack is empty, do nothing.
#After processing the entire string, convert the stack into a string using "".join(stack).
#Apply the same process to both Bob's and Alice's strings.
#Compare the resulting strings:
#If they are equal, print "YES".
#Otherwise, print "NO".

def process(s):
  stack = []
  for ch in s:
    if ch == "#" :
      if stack:
        stack.pop()
    else:
      stack.append(ch)
  return "".join(stack)
bob = input().strip()
alice = input().strip()
if process(bob) == process(alice):
  print("YES")
else:
  print("NO")

    
