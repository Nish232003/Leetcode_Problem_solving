# LeetCode 1822: Sign of the Product of an Array | Product Simulation

# Approach:
# Instead of directly determining the sign while traversing, we first compute
# the product of all elements and then determine its sign.

# 1. Initialize:
#    - Set 'product' to 1.

# 2. Traverse the array:
#    - Multiply each number with 'product'.

# 3. Determine the sign:
#    - If product > 0, return 1.
#    - If product < 0, return -1.
#    - Otherwise, return 0.

# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution:
    def arraySign(self, nums: List[int]) -> int:

        product = 1

        for num in nums:
            product *= num

        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
