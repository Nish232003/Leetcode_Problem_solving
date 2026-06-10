# LeetCode 155: Min Stack | Two Stacks for Constant Time Minimum Retrieval

# Approach:
# Instead of searching for the minimum element every time,
# we maintain an additional stack that stores the minimum value
# at each stage.

# 1. Initialize:
#    - Create two stacks:
#        • stack -> stores all values
#        • minStack -> stores the minimum value till that position

# 2. Push Operation:
#    - Push value into stack.
#    - If minStack is empty, push the value.
#    - Otherwise, push:
#        min(current value, current minimum)

# 3. Pop Operation:
#    - Remove the top element from both stacks.
#    - This keeps them synchronized.

# 4. Top Operation:
#    - Return the top element of stack.

# 5. Get Minimum:
#    - The current minimum element is always present
#      at the top of minStack.

# 6. Complexity:
#    - push()   -> O(1)
#    - pop()    -> O(1)
#    - top()    -> O(1)
#    - getMin() -> O(1)
#    - Space Complexity -> O(n)


class MinStack(object):

    def __init__(self):

        self.stack = []
        self.minStack = []

    def push(self, val):

        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(
                min(val, self.minStack[-1])
            )

    def pop(self):

        self.stack.pop()
        self.minStack.pop()

    def top(self):

        return self.stack[-1]

    def getMin(self):

        return self.minStack[-1]
