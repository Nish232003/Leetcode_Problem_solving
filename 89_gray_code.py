# LeetCode 89: Gray Code | Bit Manipulation

# Approach:
# Gray code can be generated directly using the formula:
#     gray(i) = i ^ (i >> 1)
#
# 1. Iterate through all numbers from 0 to (2^n - 1).
#
# 2. For each number i:
#    - Right shift i by 1 bit.
#    - XOR the result with i.
#    - This produces the corresponding Gray code value.
#
# 3. Store each Gray code value in the result list.
#
# 4. Return the generated sequence.
#
# Why does it work?
# - Consecutive Gray codes differ by exactly one bit.
# - The formula guarantees a valid n-bit Gray code sequence.
#
# Example (n = 2):
# i = 0 -> 00 ^ 00 = 00 -> 0
# i = 1 -> 01 ^ 00 = 01 -> 1
# i = 2 -> 10 ^ 01 = 11 -> 3
# i = 3 -> 11 ^ 01 = 10 -> 2
#
# Result: [0, 1, 3, 2]
#
# Complexity:
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)


class Solution(object):
    def grayCode(self, n):
        result = []

        for i in range(1 << n):
            result.append(i ^ (i >> 1))

        return result
