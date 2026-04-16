# LeetCode: 22. Generate Parentheses

# Approach:
# - Use Backtracking.
# - Generate all possible combinations of parentheses.
# - Ensure validity by:
#   * Adding '(' only if open < n
#   * Adding ')' only if close < open
# - This guarantees well-formed parentheses.

class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtrack(curr, open_count, close_count):
            
            if len(curr) == 2 * n:
                result.append(curr)
                return

          
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
