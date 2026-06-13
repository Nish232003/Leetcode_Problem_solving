# LeetCode 209: Minimum Size Subarray Sum | Sliding Window

# Approach:
# Since all numbers are positive, we can use a sliding window.
# Expand the window until its sum becomes >= target.
# Then shrink it from the left to find the smallest valid window.

# 1. Initialize:
#    - left = 0
#    - curr_sum = 0
#    - min_len = infinity

# 2. Expand the window:
#    - Add nums[right] to curr_sum.

# 3. While curr_sum >= target:
#    - Update min_len with current window size.
#    - Remove nums[left] from curr_sum.
#    - Move left forward.

# 4. After processing:
#    - If min_len was never updated, return 0.
#    - Otherwise return min_len.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def minSubArrayLen(self, target, nums):

        left = 0
        curr_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
