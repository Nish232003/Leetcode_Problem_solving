#Leetcode: Move Zeroes (LeetCode 283)

#- Implemented in-place solution to move all zeroes to the end
#- Maintained relative order of non-zero elements
#- Used two-pass approach with pointer tracking
#- Time Complexity: O(n)
#- Space Complexity: O(1)


class Solution(object):
    def moveZeroes(self, nums):
        p = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p] = nums[i]
                p += 1

        for j in range(p, len(nums)):
            nums[j] = 0
