# LeetCode 167: Two Sum II - Input Array Is Sorted | Two Pointers

# Approach:
# Since the array is already sorted, we can use two pointers.
#
# 1. Initialize:
#    - left = 0 (first element)
#    - right = len(numbers) - 1 (last element)
#
# 2. Calculate current sum:
#    - numbers[left] + numbers[right]
#
# 3. Compare with target:
#    - If sum == target:
#         return [left + 1, right + 1]
#         (+1 because array is 1-indexed)
#
#    - If sum < target:
#         move left pointer rightward
#         to increase the sum.
#
#    - If sum > target:
#         move right pointer leftward
#         to decrease the sum.
#
# 4. Continue until the pair is found.
#
# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def twoSum(self, numbers, target):

        left = 0
        right = len(numbers) - 1

        while left < right:

            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left + 1, right + 1]

            elif curr_sum < target:
                left += 1

            else:
                right -= 1
