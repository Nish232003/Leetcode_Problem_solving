# LeetCode 112: Path Sum | DFS (Recursive Tree Traversal)

# Approach:
# We check if there exists a root-to-leaf path whose sum equals targetSum.

# 1. Traverse the tree using DFS.
# 2. At each node:
#    - Subtract node value from targetSum.
# 3. If we reach a leaf node:
#    - Check if remaining sum equals node value.
# 4. Return True if any path satisfies condition.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(h) where h = height of tree

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        remaining = targetSum - root.val

        return (self.hasPathSum(root.left, remaining) or
                self.hasPathSum(root.right, remaining))
