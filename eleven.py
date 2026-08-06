# Approach
# Read number of interior and exterior walls.
# Read area of each interior wall and add painting cost.
# Read area of each exterior wall and add painting cost.
# If number of walls is 0, the corresponding loop will be skipped.
# Print the total estimated cost.

n = int(input())
e = int(input())

cost = 0


for _ in range(n):
    area = float(input())
    cost += area * 18


for _ in range(e):
    area = float(input())
    cost += area * 12

print("Total estimated Cost :", cost, "INR")
