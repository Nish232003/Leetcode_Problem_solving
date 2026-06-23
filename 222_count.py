# LeetCode 222: Count Complete Tree Nodes | Height Comparison + Recursion

# Approach:
# A complete binary tree has a special property:
# if the height of the leftmost path and rightmost path are equal,
# the tree is perfect and contains (2^height - 1) nodes.

# 1. Define helper functions:
#    - left_height(node): computes the height by moving left.
#    - right_height(node): computes the height by moving right.

# 2. For each subtree:
#    - Find its left and right heights.
#    - If both heights are equal:
#        • It is a perfect binary tree.
#        • Number of nodes = 2^height - 1.
#    - Otherwise:
#        • Count current node + nodes in left subtree + nodes in right subtree.

# 3. Return the total number of nodes.

# 4. Complexity:
#    - Time Complexity: O((log n)^2)
#    - Space Complexity: O(log n)


class Solution(object):
    def countNodes(self, root):

        def left_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def right_height(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        if not root:
            return 0

        lh = left_height(root)
        rh = right_height(root)

        if lh == rh:
            return (1 << lh) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
