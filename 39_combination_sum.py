# LeetCode 39: Combination Sum | Backtracking

# Approach:
# 1. Use backtracking to generate all valid combinations.
# 2. At each index:
#    - Include the current candidate multiple times.
#    - Move to the next candidate when needed.
# 3. If target becomes 0:
#    - Store the current combination.
# 4. If target becomes negative or index goes out of bounds:
#    - Stop exploring that path.
#
# 5. Complexity:
#    - Time Complexity: Exponential in the worst case.
#    - Space Complexity: O(target) for recursion stack.


class Solution:
    def combinationSum(self, candidates, target):

        ans = []

        def dfs(idx, target, path):

            if target == 0:
                ans.append(path[:])
                return

            if idx == len(candidates) or target < 0:
                return

            path.append(candidates[idx])
            dfs(idx, target - candidates[idx], path)
            path.pop()

            dfs(idx + 1, target, path)

        dfs(0, target, [])
        return ans
