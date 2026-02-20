#Add solution for LeetCode 35 - Search Insert Position

#- Implemented binary search approach to find target index or insertion position
#- Ensures O(log n) time complexity as required
#- Returns correct insert position if target is not present
#- Clean and readable Python implementation


class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
