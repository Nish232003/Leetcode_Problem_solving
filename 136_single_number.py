# LeetCode 136: Single Number | Bit Manipulation (XOR)

# Approach:
# We use the XOR operation to find the unique element.

# 1. XOR Properties:
#    - a ^ a = 0
#    - a ^ 0 = a
#    - XOR is commutative and associative.

# 2. Traverse the array:
#    - XOR every number with the current result.
#    - Duplicate numbers cancel each other out.
#    - The remaining value is the single number.

# 3. Return:
#    - The final XOR result.

# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def singleNumber(self, nums):

        result = 0

        for num in nums:
            result ^= num

        return result
