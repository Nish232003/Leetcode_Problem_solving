# LeetCode 3742: Maximum Path Score in a Grid | 3D DP (Grid + Cost Constraint)

# Approach:
# Instead of tracking only the maximum score at each cell, we also track the cost used so far.
# This is because we cannot exceed the given cost k.
# So we use a 3D DP where each state depends on position and cost.

# 1. Handle initialization:
#    - Let m, n be grid dimensions.
#    - Create a 3D DP array:
#        dp[i][j][c] = max score to reach (i,j) with cost c
#    - Initialize all values to -1 (invalid state).

# 2. Starting point:
#    - At (0,0), calculate:
#        cost = 0 if grid[0][0] == 0 else 1
#    - If cost <= k:
#        dp[0][0][cost] = grid[0][0]

# 3. Traverse the grid:
#    - For each cell (i, j) and each cost c:
#        - If dp[i][j][c] is valid:
#            - Try moving:
#                • Down → (i+1, j)
#                • Right → (i, j+1)

# 4. Transition:
#    - For next cell value = grid[ni][nj]:
#        • score added = value
#        • cost added = 0 if value == 0 else 1
#    - Compute:
#        new_cost = c + cost
#    - If new_cost <= k:
#        update dp[ni][nj][new_cost] with maximum score

# 5. Final answer:
#    - At destination (m-1, n-1):
#        take max(dp[m-1][n-1][c]) for all c <= k
#    - If all values are -1 → return -1

# 6. Complexity:
#    - Time Complexity: O(m * n * k)
#    - Space Complexity: O(m * n * k)


class Solution(object):
    def maxPathScore(self, grid, k):

        m, n = len(grid), len(grid[0])

        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]

        start_cost = 0 if grid[0][0] == 0 else 1
        if start_cost <= k:
            dp[0][0][start_cost] = grid[0][0]

        for i in range(m):
            for j in range(n):
                for c in range(k + 1):

                    if dp[i][j][c] == -1:
                        continue

                    for dx, dy in [(1, 0), (0, 1)]:
                        ni, nj = i + dx, j + dy

                        if ni < m and nj < n:
                            val = grid[ni][nj]
                            cost = 0 if val == 0 else 1
                            new_cost = c + cost

                            if new_cost <= k:
                                dp[ni][nj][new_cost] = max(
                                    dp[ni][nj][new_cost],
                                    dp[i][j][c] + val
                                )

        ans = max(dp[m - 1][n - 1])
        return ans if ans != -1 else -1
