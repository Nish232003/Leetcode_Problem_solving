#I represented the number of two-wheelers and four-wheelers as variables. Then I formed two linear equations based on the total number of vehicles and total number of wheels.
#After that, I solved the equations using substitution to find the values of both variables. 
#Finally, I validated that the computed values are non-negative and satisfy the given constraints

v = int(input())
w = int(input())
if w<2 or w%2 != 0 or v>= w:
  print("Invalid Input")
else:
  fw = (w-2*v)//2
  tw = v-fw
  if tw<0 or fw<0:
    print("Invalid Input")
  else:
    print(tw,fw)
