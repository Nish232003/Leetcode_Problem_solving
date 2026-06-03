# LeetCode 91: Decode Ways | Dynamic Programming

# Approach:
# Let dp[i] represent the number of ways to decode
# the substring s[0:i].
#
# 1. If the string starts with '0', return 0
#    because no valid encoding begins with 0.
#
# 2. Initialize:
#    - dp[0] = 1 (empty string)
#    - dp[1] = 1 (first character is valid)
#
# 3. For each position i:
#
#    Single-digit decoding:
#    - If s[i-1] is between '1' and '9',
#      add dp[i-1].
#
#    Two-digit decoding:
#    - If s[i-2:i] forms a number between
#      10 and 26, add dp[i-2].
#
# 4. dp[len(s)] gives the total number
#    of valid decodings.
#
# Example:
# s = "226"
#
# "2 2 6"  -> BBF
# "22 6"   -> VF
# "2 26"   -> BZ
#
# Answer = 3
#
# Complexity:
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0

        n = len(s)

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            two_digit = int(s[i - 2:i])

            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
