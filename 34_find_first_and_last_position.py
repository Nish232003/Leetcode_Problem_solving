# LeetCode 34: Find First and Last Position of Element in Sorted Array
# Binary Search for Leftmost and Rightmost Occurrence

# Approach:
# Since the array is sorted, we can use Binary Search.
#
# We perform two separate binary searches:
#
# 1. Find the first occurrence (leftmost index)
#    - When target is found, continue searching on the left side.
#
# 2. Find the last occurrence (rightmost index)
#    - When target is found, continue searching on the right side.
#
# 3. Return [first, last].
#
# If target does not exist, return [-1, -1].
#
# Example:
# nums = [5,7,7,8,8,10], target = 8
#
# First occurrence = 3
# Last occurrence  = 4
#
# Output = [3,4]
#
# Complexity:
# - Time Complexity: O(log n)
# - Space Complexity: O(1)


class Solution(object):
    def searchRange(self, nums, target):

        def findFirst():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def findLast():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        return [findFirst(), findLast()]
