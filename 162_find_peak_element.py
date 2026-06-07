# LeetCode 162: Find Peak Element | Binary Search

# Approach:
# Instead of checking every element linearly, we use Binary Search
# based on the slope formed by nums[mid] and nums[mid + 1].

# 1. Initialize:
#    - left = 0
#    - right = len(nums) - 1

# 2. Perform Binary Search:
#    - Find mid.
#    - Compare nums[mid] with nums[mid + 1].
#
#    Case 1:
#    - If nums[mid] > nums[mid + 1],
#      we are on a descending slope.
#      A peak must exist at mid or on the left side.
#      Move right = mid.
#
#    Case 2:
#    - If nums[mid] < nums[mid + 1],
#      we are on an ascending slope.
#      A peak must exist on the right side.
#      Move left = mid + 1.

# 3. Continue until left == right.
#    - This index represents a peak element.

# 4. Return the peak index.

# 5. Complexity:
#    - Time Complexity: O(log n)
#    - Space Complexity: O(1)


class Solution(object):
    def findPeakElement(self, nums):

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
