# LeetCode 132: Palindrome Partitioning II | DP + Expand Around Center

# Approach:
# We need the minimum number of cuts such that every resulting substring
# is a palindrome.

# 1. Initialize:
#    - dp[i] stores the minimum cuts needed for substring s[0...i].
#    - Worst case: cut before every character, so dp[i] = i.

# 2. Expand around every index as a palindrome center:
#    - Check odd-length palindromes.
#    - Check even-length palindromes.

# 3. While expanding:
#    - If palindrome starts at index 0, no cut is needed.
#    - Otherwise, update:
#         dp[right] = min(dp[right], dp[left - 1] + 1)

# 4. Continue until all palindrome centers are processed.

# 5. Return dp[n - 1].

# 6. Complexity:
#    - Time Complexity: O(n²)
#    - Space Complexity: O(n)


class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)
        dp = [i for i in range(n)]

        for center in range(n):

            left = right = center
            while left >= 0 and right < n and s[left] == s[right]:

                if left == 0:
                    dp[right] = 0
                else:
                    dp[right] = min(dp[right], dp[left - 1] + 1)

                left -= 1
                right += 1

            left, right = center, center + 1
            while left >= 0 and right < n and s[left] == s[right]:

                if left == 0:
                    dp[right] = 0
                else:
                    dp[right] = min(dp[right], dp[left - 1] + 1)

                left -= 1
                right += 1

        return dp[-1]
