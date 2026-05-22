# LeetCode 33: Search in Rotated Sorted Array | Modified Binary Search

# Approach:
# Instead of performing normal binary search directly, we identify
# which half of the array is sorted in every iteration.

# 1. Initialize:
#    - Use two pointers:
#        • left = 0
#        • right = len(nums) - 1

# 2. Perform Binary Search:
#    - Find middle index 'mid'.
#    - If nums[mid] equals target, return mid.

# 3. Identify sorted half:
#    - If nums[left] <= nums[mid]:
#         Left half is sorted.
#    - Else:
#         Right half is sorted.

# 4. Check where target lies:
#    - If target belongs to the sorted half:
#         Move search space inside that half.
#    - Otherwise:
#         Search in the opposite half.

# 5. If target is not found:
#    - Return -1.

# 6. Complexity:
#    - Time Complexity: O(log n)
#    - Space Complexity: O(1)


class Solution(object):
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:

                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:

                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
