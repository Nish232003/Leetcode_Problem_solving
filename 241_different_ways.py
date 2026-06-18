# LeetCode 241: Different Ways to Add Parentheses | Divide and Conquer + Recursion

# Approach:
# Instead of evaluating the expression with a fixed order, we recursively split
# the expression at every operator and compute all possible results from the
# left and right parts.

# 1. Base Case:
#    - If the expression contains only digits, convert it to an integer and
#      return it as a list containing one value.

# 2. Traverse the expression:
#    - Whenever an operator ('+', '-', '*') is found:
#        • Recursively compute all possible results for the left substring.
#        • Recursively compute all possible results for the right substring.

# 3. Combine results:
#    - For every result from the left side and every result from the right side:
#        • Apply the current operator.
#        • Store the computed value in the answer list.

# 4. Return all possible results.

# 5. Complexity:
#    - Time Complexity: Exponential (Catalan-like growth)
#      due to exploring all possible parenthesizations.
#    - Space Complexity: O(n)
#      for recursion stack (excluding output storage).


class Solution(object):
    def diffWaysToCompute(self, expression):

        if expression.isdigit():
            return [int(expression)]

        ans = []

        for i, ch in enumerate(expression):

            if ch in "+-*":

                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for l in left:
                    for r in right:

                        if ch == '+':
                            ans.append(l + r)

                        elif ch == '-':
                            ans.append(l - r)

                        else:
                            ans.append(l * r)

        return ans
