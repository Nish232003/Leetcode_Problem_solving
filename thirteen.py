## Approach

#1. Read the dimensions `N` and `M`, then store the input in a 2D array.
#2. Create a `Node` object for each row and store these nodes in a list.
#3. Rearrange the nodes by placing:
#   - All **even-indexed** nodes first (`0, 2, 4, ...`)
#   - Followed by all **odd-indexed** nodes (`1, 3, 5, ...`)
#4. Connect the reordered nodes to form a **Doubly Linked List** by updating the `next` and `prev` pointers.
#5. Return the head of the linked list (or traverse it to print the result).



class Node:
    def __init__(self, data):
        self.data = data      
        self.prev = None      
        self.next = None      


n = int(input())
m = int(input())

arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

nodes = []
for row in arr:
    nodes.append(Node(row))


order = []


for i in range(0, n, 2):
    order.append(nodes[i])

# Add odd-indexed nodes
for i in range(1, n, 2):
    order.append(nodes[i])

for i in range(len(order) - 1):
    order[i].next = order[i + 1]
    order[i + 1].prev = order[i]


head = order[0]

temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next
```
