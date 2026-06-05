# LeetCode 137: Single Number II | Bit Manipulation

# Approach:
# We track bits that have appeared:
#    - once  -> bits seen 1 time
#    - twice -> bits seen 2 times
#
# When a bit appears the third time, it is removed from both
# 'once' and 'twice'.
#
# This effectively counts each bit modulo 3.

# 1. Initialize:
#    - once = 0
#    - twice = 0

# 2. Traverse the array:
#    - Update 'once' using XOR and mask out bits already in 'twice'.
#    - Update 'twice' using XOR and mask out bits already in 'once'.

# 3. Return:
#    - 'once' contains the number that appears exactly once.

# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def singleNumber(self, nums):

        once = 0
        twice = 0

        for num in nums:
            once = (once ^ num) & ~twice
            twice = (twice ^ num) & ~once

        return once
