# LeetCode 40: Combination Sum II | Backtracking + Duplicate Skipping

# Approach:
# 1. Sort the array so duplicates become adjacent.
# 2. Use backtracking to build combinations.
# 3. Each number can be used only once:
#    - Move to the next index after choosing a number.
# 4. Skip duplicate values at the same recursion level.
# 5. If target becomes 0:
#    - Store the current combination.
# 6. If current number exceeds target:
#    - Stop exploring further.
#
# 7. Complexity:
#    - Time Complexity: Exponential in the worst case.
#    - Space Complexity: O(n) recursion stack.


class Solution:
    def combinationSum2(self, candidates, target):

        candidates.sort()
        ans = []

        def dfs(start, target, path):

            if target == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, target - candidates[i], path)
                path.pop()

        dfs(0, target, [])
        return ans
