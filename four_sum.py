# LeetCode 18: 4Sum

# Approach:
# 1. Sort the array to simplify duplicate handling and enable two-pointer technique.
# 2. Use two nested loops to fix the first two elements (i and j).
# 3. For remaining elements, apply two-pointer approach:
#    - left = j + 1
#    - right = n - 1
# 4. Calculate total sum of four elements:
#    - If equal to target → store result and skip duplicates
#    - If less → move left pointer forward
#    - If more → move right pointer backward
# 5. Skip duplicates at all levels (i, j, left, right) to ensure unique quadruplets.

# Time Complexity: O(n^3)
# Space Complexity: O(1) (excluding output)

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result
