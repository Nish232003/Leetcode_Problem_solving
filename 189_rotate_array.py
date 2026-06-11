# LeetCode 189: Rotate Array | Reversal Algorithm

# Approach:
# Instead of rotating one step at a time, we use the reversal technique.
#
# 1. Handle large k:
#    - Rotating n times gives the same array.
#    - So use k = k % len(nums).
#
# 2. Reverse the entire array.
#
# 3. Reverse the first k elements.
#
# 4. Reverse the remaining n-k elements.
#
# 5. The array becomes rotated to the right by k positions.
#
# Example:
# nums = [1,2,3,4,5,6,7], k = 3
#
# Reverse all:
# [7,6,5,4,3,2,1]
#
# Reverse first k:
# [5,6,7,4,3,2,1]
#
# Reverse remaining:
# [5,6,7,1,2,3,4]
#
# Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def rotate(self, nums, k):

        n = len(nums)
        k %= n

        def reverse(left, right):

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
