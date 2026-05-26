# LeetCode 31: Next Permutation | Pivot + Reverse Technique

# Approach:
# We find the next lexicographically greater permutation
# by modifying the array in-place.

# 1. Find the pivot:
#    - Traverse from right to left.
#    - Find the first index 'pivot' such that:
#          nums[pivot] < nums[pivot + 1]
#    - This indicates where increasing order breaks.

# 2. Handle descending order case:
#    - If no pivot exists, array is in highest permutation.
#    - Reverse the entire array to get lowest permutation.

# 3. Find the next greater element:
#    - Traverse again from the right side.
#    - Find the first element greater than nums[pivot].
#    - Swap both elements.

# 4. Reverse the suffix:
#    - Reverse elements after pivot index.
#    - This gives the smallest lexicographical arrangement.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def nextPermutation(self, nums):

        n = len(nums)

        
        pivot = -1

        for i in range(n - 2, -1, -1):

            if nums[i] < nums[i + 1]:
                pivot = i
                break

        
        if pivot == -1:
            nums.reverse()
            return

        
        for i in range(n - 1, pivot, -1):

            if nums[i] > nums[pivot]:

                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        
        left = pivot + 1
        right = n - 1

        while left < right:

            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1
