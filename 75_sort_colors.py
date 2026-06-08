# LeetCode 75: Sort Colors | Dutch National Flag Algorithm

# Approach:
# Since the array contains only three values (0, 1, and 2),
# we can sort it in a single traversal using three pointers.
#
# 1. Initialize:
#    - low: position where next 0 should be placed.
#    - mid: current element being processed.
#    - high: position where next 2 should be placed.
#
# 2. Traverse while mid <= high:
#
#    Case 1: nums[mid] == 0
#    - Swap nums[low] and nums[mid].
#    - Increment both low and mid.
#
#    Case 2: nums[mid] == 1
#    - It is already in the correct region.
#    - Increment mid.
#
#    Case 3: nums[mid] == 2
#    - Swap nums[mid] and nums[high].
#    - Decrement high.
#    - Do not increment mid because the swapped element
#      needs to be checked.
#
# 3. After traversal:
#    - All 0s are on the left.
#    - All 1s are in the middle.
#    - All 2s are on the right.
#
# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def sortColors(self, nums):

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:

                nums[low], nums[mid] = nums[mid], nums[low]

                low += 1
                mid += 1

            elif nums[mid] == 1:

                mid += 1

            else:

                nums[mid], nums[high] = nums[high], nums[mid]

                high -= 1
