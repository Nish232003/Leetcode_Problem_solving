# LeetCode 396: Rotate Function | Math + Recurrence Optimization

# Approach:
# Instead of constructing each rotated array and recalculating the function,
# we use a recurrence relation to efficiently compute the next value.

# 1. Handle edge case:
#    - If n == 1, return 0 directly.

# 2. Initialize:
#    - Compute total_sum of all elements in nums.
#    - Compute initial rotation value F(0).
#    - Use 'max_val' to store the maximum result.

# 3. Key Observation:
#    - F(k) = F(k-1) + total_sum - n * nums[n - k]
#    - This avoids recomputation and gives O(1) transition.

# 4. Traverse the array:
#    - Update F using the above formula.
#    - Update max_val at each step.

# 5. Return result:
#    - Return the maximum value among all rotations.

# 6. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def maxRotateFunction(self, nums):

        n = len(nums)

        if n == 1:
            return 0


        total_sum = sum(nums)


        
        F = 0
        for i in range(n):
            F += i * nums[i]

        max_val = F


        
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            max_val = max(max_val, F)


        return max_val
