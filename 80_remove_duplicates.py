# LeetCode 80: Remove Duplicates from Sorted Array II | Two Pointer In-Place Optimization

# Approach:
# Since the array is sorted, duplicates are adjacent. We need to ensure each element
# appears at most twice while keeping order and doing it in-place.

# 1. Use a write pointer k:
#    - k represents the position where we place the next valid element.

# 2. Traverse the array:
#    - For each element x:
#        • If we have written fewer than 2 elements, always keep it.
#        • Otherwise, compare with nums[k - 2]:
#              - If x != nums[k - 2], it means we have not exceeded 2 duplicates.
#              - Otherwise, skip it.

# 3. Modify array in-place:
#    - Overwrite nums[k] with valid elements.

# 4. Return k:
#    - First k elements are the valid result.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        k = 0

        for x in nums:
            if k < 2 or x != nums[k - 2]:
                nums[k] = x
                k += 1

        return k
