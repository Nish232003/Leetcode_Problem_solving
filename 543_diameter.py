# LeetCode 543: Diameter of Binary Tree | DFS + Height Calculation

# Approach:
# Instead of checking every possible path separately, we use DFS to calculate
# the height of each subtree while simultaneously updating the maximum diameter.

# 1. Initialize:
#    - Create a variable 'ans' to store the maximum diameter found so far.

# 2. Define a recursive function height(node):
#    - If node is None, return 0.
#    - Recursively find the height of the left subtree.
#    - Recursively find the height of the right subtree.

# 3. Compute diameter through current node:
#    - Diameter at current node = left_height + right_height
#    - Update 'ans' if this value is larger.

# 4. Return height of current subtree:
#    - Height = 1 + max(left_height, right_height)

# 5. Start DFS from the root and return the maximum diameter.

# 6. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(h)
#      where h is the height of the tree (O(log n) for balanced tree,
#      O(n) in the worst case).


class Solution(object):
    def diameterOfBinaryTree(self, root):

        self.ans = 0

        def height(node):

            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            self.ans = max(self.ans, left_height + right_height)

            return 1 + max(left_height, right_height)

        height(root)

        return self.ans
