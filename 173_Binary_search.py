# LeetCode 173: Binary Search Tree Iterator | Inorder Traversal + Stack

# Approach:
# Since the inorder traversal of a BST gives nodes in sorted order,
# we simulate the inorder traversal using a stack.

# 1. Initialize:
#    - Create an empty stack.
#    - Push all left nodes from the root to the leftmost node.
#
# 2. next():
#    - Pop the top node from the stack.
#    - This node is the next smallest element.
#    - If the popped node has a right child:
#        • Push the right child and all its left descendants.
#    - Return the popped node's value.
#
# 3. hasNext():
#    - If stack is not empty, there is a next element.
#    - Otherwise return False.
#
# 4. Why does this work?
#    - The stack always stores the path to the next smallest node.
#    - After visiting a node, we process its right subtree.
#
# 5. Complexity:
#    - next()    -> Average O(1)
#    - hasNext() -> O(1)
#    - Space Complexity -> O(h)
#
# where h is the height of the tree.


class BSTIterator:

    def __init__(self, root):

        self.stack = []
        self.pushLeft(root)

    def pushLeft(self, node):

        while node:
            self.stack.append(node)
            node = node.left

    def next(self):

        node = self.stack.pop()

        if node.right:
            self.pushLeft(node.right)

        return node.val

    def hasNext(self):

        return len(self.stack) > 0
