# LeetCode 153: Find Minimum in Rotated Sorted Array | Binary Search

# Approach:
# Since the array is sorted and then rotated, the minimum element
# lies in the unsorted portion of the array.
# We use Binary Search to efficiently locate it.

# 1. Initialize:
#    - Use two pointers:
#        • left  -> starting index
#        • right -> ending index

# 2. Binary Search:
#    - Find the middle index 'mid'.
#
#    - Compare nums[mid] with nums[right]:
#
#      • If nums[mid] > nums[right]:
#          - Minimum lies in the right half.
#          - Move left = mid + 1
#
#      • Otherwise:
#          - Minimum lies at mid or in the left half.
#          - Move right = mid

# 3. Loop ends:
#    - When left == right,
#      that index contains the minimum element.

# 4. Return:
#    - Return nums[left]

# 5. Complexity:
#    - Time Complexity: O(log n)
#    - Space Complexity: O(1)


class Solution(object):
    def findMin(self, nums):
       
        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
