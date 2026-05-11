# LeetCode 1137: N-th Tribonacci Number
# Approach: Recursion

# Intuition:
# Tribonacci numbers follow the relation:
# T(n) = T(n-1) + T(n-2) + T(n-3)
#
# We recursively calculate the previous three Tribonacci numbers
# until reaching the base cases.

class Solution(object):
    def tribonacci(self, n):

        # Base cases
        if n == 0:
            return 0

        elif n == 1 or n == 2:
            return 1

        # Recursive calls
        return (
            self.tribonacci(n - 1) +
            self.tribonacci(n - 2) +
            self.tribonacci(n - 3)
        )
