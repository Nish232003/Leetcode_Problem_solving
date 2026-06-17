# LeetCode 113: Path Sum II | DFS + Backtracking

# Approach:
# We need to collect ALL root-to-leaf paths whose sum equals targetSum.

# 1. Use DFS traversal from root to leaf.
# 2. Maintain:
#    - current path list
#    - remaining target sum
#
# 3. At each node:
#    - Add node value to path
#    - Recurse left and right with updated sum
#
# 4. If leaf node and sum matches:
#    - Store a copy of current path
#
# 5. Backtrack:
#    - Remove last element before returning to previous state

# 6. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(h) recursion stack (excluding output)

class Solution(object):
    def pathSum(self, root, targetSum):
        res = []
        path = []

        def dfs(node, remaining):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right and node.val == remaining:
                res.append(path[:])
            else:
                dfs(node.left, remaining - node.val)
                dfs(node.right, remaining - node.val)

            path.pop()

        dfs(root, targetSum)
        return res
