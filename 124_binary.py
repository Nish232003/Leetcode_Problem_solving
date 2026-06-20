# LeetCode 124: Binary Tree Maximum Path Sum | DFS + Divide and Conquer

# Approach:
# We use DFS to compute the maximum gain obtainable from each node.

# 1. For each node:
#    - Recursively calculate the maximum gain from the left subtree.
#    - Recursively calculate the maximum gain from the right subtree.
#    - Ignore negative gains by taking max(0, gain).

# 2. Compute path through current node:
#    - Current path sum = node.val + left_gain + right_gain.
#    - Update the global maximum if this path is better.

# 3. Return contribution to parent:
#    - A parent can only extend one side of the path.
#    - Return node.val + max(left_gain, right_gain).

# 4. The answer is the maximum path sum encountered during DFS.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(h), where h is the height of the tree
#      (O(n) in worst case, O(log n) for balanced trees).

class Solution(object):
    def maxPathSum(self, root):
        self.ans = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            self.ans = max(self.ans, node.val + left_gain + right_gain)

            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.ans
