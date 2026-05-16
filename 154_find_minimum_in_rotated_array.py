# LeetCode 154: Find Minimum in Rotated Sorted Array II | Binary Search + Duplicate Handling

# Approach:
# Instead of checking every element linearly, we use Binary Search
# to efficiently locate the minimum element in the rotated array.

# 1. Initialize pointers:
#    - 'left' starts from beginning.
#    - 'right' starts from end.

# 2. Apply Binary Search:
#    - Find middle index 'mid'.

# 3. Compare nums[mid] with nums[right]:
#    
#    Case 1:
#    - If nums[mid] > nums[right]
#      → Minimum lies in right half.
#      → Move left = mid + 1
#
#    Case 2:
#    - If nums[mid] < nums[right]
#      → Minimum lies in left half including mid.
#      → Move right = mid
#
#    Case 3:
#    - If nums[mid] == nums[right]
#      → Duplicate values create ambiguity.
#      → Reduce search space safely using right -= 1

# 4. Loop ends when left == right:
#    - That index contains the minimum element.

# 5. Complexity:
#    - Average Time Complexity: O(log n)
#    - Worst Case Time Complexity: O(n)   (due to duplicates)
#    - Space Complexity: O(1)


class Solution(object):
    def findMin(self, nums):
        
        left = 0
        right = len(nums) - 1

        
        while left < right:

            mid = left + (right - left) // 2

            
            if nums[mid] > nums[right]:
                left = mid + 1

            
            elif nums[mid] < nums[right]:
                right = mid

            
            else:
                right -= 1

        
        return nums[left]
