# LeetCode 509: Fibonacci Number
# Approach: Recursion

# Intuition:
# Fibonacci numbers follow the relation:
# F(n) = F(n-1) + F(n-2)
#
# We recursively calculate the previous two Fibonacci numbers
# until reaching the base cases.

class Solution(object):
    def fib(self, n):
     
        if n <= 1 or n == 0:
            return n

        return self.fib(n - 1) + self.fib(n - 2)
