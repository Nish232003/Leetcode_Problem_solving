# LeetCode 139: Word Break | Dynamic Programming (Bottom-Up)

# Approach:
# We use Dynamic Programming to determine whether the string can be
# segmented into valid dictionary words.

# 1. Convert wordDict into a set for O(1) lookup.
#
# 2. Create a DP array:
#    - dp[i] = True if the substring s[0:i] can be segmented
#      using words from the dictionary.
#
# 3. Base Case:
#    - dp[0] = True
#      (An empty string is always considered segmented.)
#
# 4. For each position i:
#    - Check all possible previous split positions j.
#    - If:
#         dp[j] is True
#         AND
#         s[j:i] exists in the dictionary
#      then mark dp[i] = True.
#
# 5. Return dp[len(s)].
#
# 6. Complexity:
#    - Time Complexity: O(n²)
#    - Space Complexity: O(n)


class Solution(object):
    def wordBreak(self, s, wordDict):

        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):

            for j in range(i):

                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
