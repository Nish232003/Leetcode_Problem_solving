# LeetCode 10: Regular Expression Matching | Recursion + Dynamic Programming (Memoization)

# Approach:
# We use recursion with memoization (top-down DP) to match string s with pattern p.

# 1. Define a recursive function dp(i, j):
#    - Returns True if s[i:] matches p[j:], else False.

# 2. Base Case:
#    - If pattern is exhausted (j == len(p)):
#      return True only if string is also exhausted (i == len(s))

# 3. Check first character match:
#    - first_match = (i < len(s)) and (s[i] == p[j] or p[j] == '.')

# 4. Handle '*' wildcard:
#    - If next character in pattern is '*':
#        We have two choices:
#        a) Skip "x*" → dp(i, j+2)
#        b) Use '*' if first_match → dp(i+1, j)

# 5. If no '*':
#    - Move both pointers if characters match → dp(i+1, j+1)

# 6. Use memoization to avoid recomputation.

class Solution(object):
    def isMatch(self, s, p):

        memo = {}

        def dp(i, j):

          
            if (i, j) in memo:
                return memo[(i, j)]

        
            if j == len(p):
                return i == len(s)

            first_match = (i < len(s)) and (s[i] == p[j] or p[j] == '.')

       
            if (j + 1) < len(p) and p[j + 1] == '*':
                
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:

                ans = first_match and dp(i + 1, j + 1)

           
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
