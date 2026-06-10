# LeetCode 191: Number of 1 Bits | Bit Manipulation

# Approach:
# We count the number of set bits (1s) in the binary representation.
#
# 1. Initialize:
#    - Create a variable 'count' = 0.
#
# 2. Traverse all bits:
#    - Check the last bit using:
#          n & 1
#    - If it is 1, increment count.
#    - Shift n right by 1 position.
#
# 3. Continue until n becomes 0.
#
# 4. Return:
#    - count contains the total number of set bits.
#
# 5. Complexity:
#    - Time Complexity: O(log n)
#    - Space Complexity: O(1)


class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        while n:

            count += (n & 1)

            n >>= 1

        return count
