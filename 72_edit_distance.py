# LeetCode 72: Edit Distance
# Dynamic Programming (Bottom-Up)

# Approach:
# We use Dynamic Programming where:
#
# dp[i][j] represents the minimum operations required
# to convert word1[0:i] into word2[0:j].
#
# Allowed operations:
# 1. Insert
# 2. Delete
# 3. Replace
#
# Transition:
#
# If characters match:
# dp[i][j] = dp[i-1][j-1]
#
# Else:
# dp[i][j] = 1 + min(
#     dp[i-1][j],     # Delete
#     dp[i][j-1],     # Insert
#     dp[i-1][j-1]    # Replace
# )
#
# Base Cases:
#
# dp[i][0] = i
# (delete all characters)
#
# dp[0][j] = j
# (insert all characters)
#
# Complexity:
# - Time Complexity: O(m * n)
# - Space Complexity: O(m * n)


class Solution(object):
    def minDistance(self, word1, word2):

        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    )

        return dp[m][n]
