# LeetCode 1464: Maximum Product of Two Elements in an Array | One Pass Maximum Tracking

# Approach:
# Instead of sorting the array, we keep track of the largest and second
# largest elements while traversing the array once.

# 1. Initialize:
#    - Set 'first' and 'second' to 0.
#    - 'first' stores the largest element seen so far.
#    - 'second' stores the second largest element.

# 2. Traverse the array:
#    - If the current number is greater than 'first':
#        • Update 'second' to 'first'.
#        • Update 'first' to the current number.
#    - Otherwise, if the current number is greater than 'second':
#        • Update 'second' to the current number.

# 3. Compute the answer:
#    - Return (first - 1) * (second - 1).

# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        first = 0
        second = 0

        for num in nums:

            if num > first:
                second = first
                first = num

            elif num > second:
                second = num

        return (first - 1) * (second - 1)
