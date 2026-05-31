# LeetCode 62: Unique Paths | Dynamic Programming

# Approach:
# We use Dynamic Programming to count the number of ways
# to reach each cell in the grid.

# Key Idea:
# A robot can only move:
#    - Right
#    - Down
#
# Therefore:
#    paths[i][j] = paths[i-1][j] + paths[i][j-1]

# 1. Initialize:
#    - Create a DP grid of size m x n.
#    - Fill first row and first column with 1
#      because there is only one way to reach them.

# 2. Fill remaining cells:
#    - Each cell gets paths from:
#         • top cell
#         • left cell

# 3. Final answer:
#    - Bottom-right cell contains total unique paths.

# 4. Complexity:
#    - Time Complexity: O(m * n)
#    - Space Complexity: O(m * n)


class Solution(object):
    def uniquePaths(self, m, n):

        
        dp = [[1] * n for _ in range(m)]

        
        for i in range(1, m):
            for j in range(1, n):

                
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        
        return dp[m - 1][n - 1]
