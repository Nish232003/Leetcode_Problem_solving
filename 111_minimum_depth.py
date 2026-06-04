# LeetCode 111: Minimum Depth of Binary Tree | DFS (Recursive)

# Approach:
# The minimum depth is the number of nodes along the shortest path
# from the root node to the nearest leaf node.
#
# 1. Handle edge case:
#    - If the tree is empty, return 0.
#
# 2. Check if current node is a leaf:
#    - If both left and right children are None, return 1.
#
# 3. Handle nodes with only one child:
#    - If left child is missing, recurse on right subtree.
#    - If right child is missing, recurse on left subtree.
#
# 4. If both children exist:
#    - Find the minimum depth of left and right subtrees.
#    - Add 1 for the current node.
#
# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(h)
#      where h is the height of the tree.


class Solution(object):
    def minDepth(self, root):

        if not root:
            return 0

        # Leaf node
        if not root.left and not root.right:
            return 1

        # Only right child exists
        if not root.left:
            return 1 + self.minDepth(root.right)

        # Only left child exists
        if not root.right:
            return 1 + self.minDepth(root.left)

        # Both children exist
        return 1 + min(
            self.minDepth(root.left),
            self.minDepth(root.right)
        )
