# LeetCode 97: Interleaving String | Dynamic Programming

# Approach:
# We use Dynamic Programming to check whether s3 can be formed
# by interleaving characters of s1 and s2 while maintaining order.

# 1. Edge Case:
#    - If len(s1) + len(s2) != len(s3), interleaving is impossible.

# 2. Initialize DP Array:
#    - dp[j] represents whether:
#         s1[0:i] and s2[0:j]
#      can form s3[0:i+j].
#    - Use 1D DP to optimize space.

# 3. Fill First Row:
#    - Match characters only using s2.

# 4. Traverse s1 and s2:
#    - Two choices for current character:
#        • Take from s1
#        • Take from s2
#    - If either forms a valid interleaving, mark dp[j] = True.

# 5. Final Answer:
#    - dp[-1] tells whether full s3 can be formed.

# 6. Complexity:
#    - Time Complexity: O(len(s1) * len(s2))
#    - Space Complexity: O(len(s2))


class Solution(object):
    def isInterleave(self, s1, s2, s3):

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [False] * (len(s2) + 1)
        dp[0] = True

        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):

            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, len(s2) + 1):

                dp[j] = (
                    (dp[j] and s1[i - 1] == s3[i + j - 1]) or
                    (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                )

        return dp[-1]
