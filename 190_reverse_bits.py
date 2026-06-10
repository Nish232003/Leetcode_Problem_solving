# LeetCode 190: Reverse Bits | Bit Manipulation

# Approach:
# We build the reversed number bit by bit.
#
# 1. Initialize:
#    - Create a variable 'result' = 0.
#
# 2. Traverse all 32 bits:
#    - Extract the last bit of n using:
#          n & 1
#    - Shift result left by 1 position.
#    - Add the extracted bit to result.
#    - Shift n right by 1 position.
#
# 3. After processing all 32 bits:
#    - result contains the reversed binary representation.
#
# 4. Return:
#    - Return result.
#
# 5. Complexity:
#    - Time Complexity: O(32) = O(1)
#    - Space Complexity: O(1)


class Solution:
    def reverseBits(self, n: int) -> int:

        result = 0

        for _ in range(32):

            result <<= 1
            result |= (n & 1)

            n >>= 1

        return result
