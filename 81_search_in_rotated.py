# LeetCode 81: Search in Rotated Sorted Array II | Modified Binary Search

# Approach:
# The array is sorted but rotated and may contain duplicates, which complicates
# normal binary search because we can’t always determine which side is sorted.

# 1. Use two pointers:
#    - left = start of array
#    - right = end of array

# 2. While searching:
#    - Compute mid.
#    - If nums[mid] == target → return True.

# 3. Handle ambiguity due to duplicates:
#    - If nums[left] == nums[mid] == nums[right],
#      we cannot determine sorted half → shrink both sides.

# 4. Otherwise:
#    - If left half is sorted:
#        • check if target lies in left half → move right
#        • else move left
#    - Else right half is sorted:
#        • check if target lies in right half → move left
#        • else move right

# 5. Complexity:
#    - Average: O(log n)
#    - Worst case (all duplicates): O(n)

class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

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

        return False
