# LeetCode 115: Distinct Subsequences | Recursion + Memoization

# Approach:
# We recursively count the number of ways to form string t from string s.

# 1. Base cases:
#    - If all characters of t are matched, return 1 since one valid
#      subsequence has been found.
#    - If s is exhausted before t, return 0 because forming t is impossible.

# 2. Memoization:
#    - Store results for each pair of indices (i, j), where:
#        i = current index in s
#        j = current index in t
#    - This avoids recomputing overlapping subproblems.

# 3. Recursive choices:
#    - If s[i] == t[j]:
#         a) Use s[i] to match t[j]
#         b) Skip s[i]
#      Total ways = both possibilities added together.
#
#    - Otherwise:
#         Skip s[i] and move forward in s.

# 4. Return the total number of ways.

# 5. Complexity:
#    - Time Complexity: O(m × n)
#    - Space Complexity: O(m × n)

class Solution(object):
    def numDistinct(self, s, t):

        memo = {}

        def dfs(i, j):

            
            if j == len(t):
                return 1

            
            if i == len(s):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == t[j]:

                memo[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)

            else:

     
                memo[(i, j)] = dfs(i + 1, j)

            return memo[(i, j)]

        return dfs(0, 0)
