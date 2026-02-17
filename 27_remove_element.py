# LeetCode 27 - Remove Element
# Approach: Two Pointer (overwrite non-val elements in-place)
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def removeElement(self, nums, val):
        k = 0  # index for placing elements not equal to val
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
