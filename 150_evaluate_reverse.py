# LeetCode 150: Evaluate Reverse Polish Notation | Stack

# Approach:
# Reverse Polish Notation (Postfix Expression) can be evaluated
# efficiently using a stack.
#
# 1. Traverse each token in the input list.
#
# 2. If the token is a number:
#    - Push it onto the stack.
#
# 3. If the token is an operator:
#    - Pop the top two numbers from the stack.
#    - Perform the operation.
#    - Push the result back onto the stack.
#
# 4. After processing all tokens:
#    - The stack will contain exactly one element,
#      which is the final answer.
#
# 5. Note:
#    - Division must truncate toward zero.
#    - Use int(a / b) instead of // because
#      // rounds toward negative infinity.
#
# 6. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


class Solution(object):
    def evalRPN(self, tokens):

        stack = []

        for token in tokens:

            if token in ["+", "-", "*", "/"]:

                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(a - b)

                elif token == "*":
                    stack.append(a * b)

                else:
                    stack.append(int(a / b))

            else:
                stack.append(int(token))

        return stack[-1]
