# LeetCode 70: Climbing Stairs | Dynamic Programming (Fibonacci)

# Approach:
# To reach the nth step, we have only two possibilities:
#
# 1. Come from (n - 1)th step by taking 1 step.
# 2. Come from (n - 2)th step by taking 2 steps.
#
# Therefore:
# ways(n) = ways(n - 1) + ways(n - 2)
#
# This follows the Fibonacci pattern.
#
# 1. Handle base cases:
#    - n = 1 → 1 way
#    - n = 2 → 2 ways
#
# 2. Use two variables to store the previous two answers.
#
# 3. Iterate from step 3 to n:
#    - Current ways = previous + second previous
#
# 4. Return the final answer.
#
# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def climbStairs(self, n):

        if n <= 2:
            return n

        first = 1   
        second = 2  

        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current

        return second
