# LeetCode 99: Recover Binary Search Tree | Inorder Traversal

# Approach:
# In a valid BST, inorder traversal gives nodes in sorted order.
# If two nodes are swapped, the inorder sequence becomes invalid
# at one or two positions.

# 1. Perform inorder traversal:
#    - Track previous visited node using 'prev'.

# 2. Detect violations:
#    - If prev.val > current.val:
#         • First violation:
#             first = prev
#             second = current
#         • Second violation:
#             second = current

# 3. Swap misplaced nodes:
#    - Swap values of first and second nodes.

# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(h)
#      where h = height of tree (recursion stack)


class Solution(object):

    def recoverTree(self, root):

        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

        def inorder(node):

            if not node:
                return

            inorder(node.left)

            if self.prev.val > node.val:

                if not self.first:
                    self.first = self.prev

                self.second = node

            self.prev = node

            inorder(node.right)

        inorder(root)

        self.first.val, self.second.val = self.second.val, self.first.val
