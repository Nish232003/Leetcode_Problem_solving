# LeetCode 221: Maximal Square | Dynamic Programming

# Approach:
# Instead of checking every possible square, use DP to store the side length
# of the largest square ending at each cell.

# 1. Initialize:
#    - Create a DP table of size (m+1) x (n+1) filled with 0.
#    - Maintain 'max_side' to track the largest square side length found.

# 2. Traverse the matrix:
#    - If matrix[i-1][j-1] is '1', then the current square size depends on:
#        • Top cell      -> dp[i-1][j]
#        • Left cell     -> dp[i][j-1]
#        • Top-left cell -> dp[i-1][j-1]
#    - Current square side:
#        dp[i][j] = 1 + min(top, left, top-left)
#    - Update max_side if a larger square is found.

# 3. If matrix[i-1][j-1] is '0', dp[i][j] remains 0.

# 4. Return the area of the largest square:
#        max_side * max_side

# 5. Complexity:
#    - Time Complexity: O(m × n)
#    - Space Complexity: O(m × n)


class Solution(object):
    def maximalSquare(self, matrix):

        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_side = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    )

                    max_side = max(max_side, dp[i][j])

        return max_side * max_side
