# LeetCode 41: First Missing Positive | Cyclic Placement

# Approach:
# 1. Place each positive number x at index x - 1
#    whenever 1 <= x <= n.
# 2. Keep swapping until every valid number is in
#    its correct position.
# 3. Traverse the array:
#    - The first index i where nums[i] != i + 1
#      gives the missing positive number.
# 4. If all positions are correct,
#    return n + 1.
#
# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution:
    def firstMissingPositive(self, nums):

        n = len(nums)
        i = 0

        while i < n:
            pos = nums[i] - 1

            if 1 <= nums[i] <= n and nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
