# LeetCode 120: Triangle | Bottom-Up Dynamic Programming

# Approach:
# We solve from bottom to top, reducing the triangle into a single minimum path row.

# Key idea:
# - Start from last row
# - For each element in upper rows:
#     choose min of two adjacent elements from row below

# 1. Copy last row as initial DP state
# 2. Move upward row by row
# 3. Update dp in-place

# 4. Complexity:
#    - Time Complexity: O(n^2)
#    - Space Complexity: O(n)

class Solution(object):
    def minimumTotal(self, triangle):
        dp = triangle[-1][:]

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]
