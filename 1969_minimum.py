# LeetCode 1969: Minimum Non-Zero Product of the Array Elements | Mathematical Observation + Fast Exponentiation

# Approach:
# Instead of simulating bit swaps, we use the pattern formed after minimizing
# the product.

# 1. Observe:
#    - The maximum number in the array is:
#          max_num = 2^p - 1
#    - To minimize the product while keeping it non-zero:
#        • Keep one copy of max_num unchanged.
#        • Pair the remaining numbers so that they become:
#              (2^p - 2)
#          repeated (2^(p-1) - 1) times.
#        • The corresponding partners become 1.

# 2. Formula:
#    - Let:
#          max_num = 2^p - 1
#          second_max = 2^p - 2
#          count = 2^(p-1) - 1
#
#    - Answer:
#          max_num × (second_max)^count

# 3. Use modular exponentiation:
#    - Since p can be as large as 60, the exponent is huge.
#    - Use fast exponentiation (pow with modulo) to compute efficiently.

# 4. Complexity:
#    - Time Complexity: O(log(2^(p-1))) = O(p)
#    - Space Complexity: O(1)


class Solution:
    def minNonZeroProduct(self, p: int) -> int:

        MOD = 10**9 + 7

        max_num = (1 << p) - 1
        second_max = max_num - 1
        count = (1 << (p - 1)) - 1

        return (max_num % MOD) * pow(second_max, count, MOD) % MOD
