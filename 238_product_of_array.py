# LeetCode 238: Product of Array Except Self | Prefix and Suffix Products

# Approach:
# Instead of using division, we compute the product of all elements to the left
# and right of each index separately and combine them.

# 1. Initialize:
#    - Create an answer array 'res' filled with 1s.
#    - Use 'prefix' to store the product of elements before the current index.

# 2. Left-to-Right Traversal:
#    - For each index i:
#        • Store the current prefix product in res[i].
#        • Update prefix by multiplying nums[i].

# 3. Right-to-Left Traversal:
#    - Use 'suffix' to store the product of elements after the current index.
#    - For each index i from n-1 to 0:
#        • Multiply res[i] by the current suffix product.
#        • Update suffix by multiplying nums[i].

# 4. Return the result array.
#    - Each res[i] contains:
#      (product of all elements to the left) ×
#      (product of all elements to the right)

# 5. Complexity:
#    - Time Complexity: O(n)
#      Two linear traversals.
#    - Space Complexity: O(1)
#      Excluding the output array.


class Solution(object):
    def productExceptSelf(self, nums):

        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
