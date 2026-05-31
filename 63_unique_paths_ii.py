# LeetCode 63: Unique Paths II | Dynamic Programming

# Approach:
# Similar to Unique Paths, but now some cells contain obstacles.
#
# Rules:
#    - 0 → empty cell
#    - 1 → obstacle
#
# A robot can only move:
#    - Right
#    - Down

# 1. Handle edge case:
#    - If starting cell has obstacle, return 0.

# 2. Initialize:
#    - Create DP grid of same size.
#    - dp[0][0] = 1 (starting point)

# 3. Traverse the grid:
#    - If current cell is obstacle:
#         dp[i][j] = 0
#    - Otherwise:
#         paths = top + left
#
# Formula:
#    dp[i][j] = dp[i-1][j] + dp[i][j-1]

# 4. Final answer:
#    - Bottom-right cell stores total unique paths.

# 5. Complexity:
#    - Time Complexity: O(m * n)
#    - Space Complexity: O(m * n)


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        
        if obstacleGrid[0][0] == 1:
            return 0

        
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        
        for i in range(m):
            for j in range(n):

                
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0

                
                else:

                    
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]

                    
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]

        
        return dp[m - 1][n - 1]
