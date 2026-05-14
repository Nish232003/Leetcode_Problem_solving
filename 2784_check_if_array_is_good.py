#LeetCode 2784 - Check if Array is Good

#Approach:
#- Sort the given array to easily verify the sequence.
#- Let the maximum element be `n`.
#- A valid good array must:
#  1. Have length exactly `n + 1`
#  2. Contain numbers from `1` to `n - 1` exactly once
#  3. Contain the number `n` exactly twice
#- Traverse the sorted array and check whether elements follow the expected pattern.
#- Return `True` if all conditions are satisfied, otherwise return `False`.


class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nums.sort()
        
        n = nums[-1]
        
        if len(nums) != n + 1:
            return False
        
        for i in range(n):
            if nums[i] != i + 1:
                return False
        
        return nums[-1] == nums[-2]
