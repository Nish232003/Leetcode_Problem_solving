# LeetCode 50: Pow(x, n) | Binary Exponentiation

# Approach:
# Instead of multiplying x n times (O(n)), use binary exponentiation
# to reduce the time complexity to O(log n).

# 1. Handle Negative Power:
#    - If n < 0:
#        • Convert x to 1/x
#        • Make n positive (n = -n)

# 2. Initialize:
#    - result = 1 (stores final answer)

# 3. Binary Exponentiation:
#    - While n > 0:
#        • If n is odd (n % 2 == 1):
#            → multiply result with current x
#        • Square x (x = x * x)
#        • Divide n by 2 (n //= 2)

# 4. Return Result:
#    - result contains x^n

# 5. Complexity:
#    - Time Complexity: O(log n)
#    - Space Complexity: O(1)


class Solution(object):
    def myPow(self, x, n):

        # 1. Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n

        # 2. Initialize result
        result = 1

        # 3. Binary exponentiation
        while n > 0:
            if n % 2 == 1:   # if n is odd
                result *= x
            x *= x           # square the base
            n //= 2          # halve the exponent

        # 4. Return final answer
        return result
