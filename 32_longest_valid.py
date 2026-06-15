# LeetCode 32: Longest Valid Parentheses | Stack of Indices

# Approach:
# Instead of checking all possible substrings, we use a stack to keep track
# of indices that help determine valid parentheses lengths efficiently.
#
# 1. Initialize:
#    - Push -1 into the stack as a base index.
#    - This helps calculate lengths correctly when a valid substring starts
#      from index 0.
#
# 2. Traverse the string:
#    - If current character is '(':
#         • Push its index onto the stack.
#
#    - If current character is ')':
#         • Pop one index from the stack.
#
#         • If stack becomes empty:
#              - Push current index as the new base.
#
#         • Otherwise:
#              - Calculate current valid length:
#                    length = current_index - stack[-1]
#              - Update maximum answer.
#
# 3. Why it works:
#    - Stack stores indices of unmatched '('.
#    - The top of the stack always represents the boundary before the
#      current valid substring.
#
# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


class Solution(object):
    def longestValidParentheses(self, s):

        stack = [-1]
        ans = 0

        for i, ch in enumerate(s):

            if ch == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)

                else:
                    ans = max(ans, i - stack[-1])

        return ans
