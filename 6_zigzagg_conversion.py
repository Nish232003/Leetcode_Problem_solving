# LeetCode 6: Zigzag Conversion | Simulation + Direction Tracking

# Approach:
# Instead of constructing the zigzag pattern in a matrix, we simulate the traversal
# row by row using a direction-based approach.
# 1. Handle edge case:
#    - If numRows == 1 or numRows >= len(s), return the original string.
# 2. Initialize:
#    - Create a list 'rows' to store characters for each row.
#    - Use 'curr_row' to track the current row.
#    - Use 'direction' to control movement (down = 1, up = -1).
# 3. Traverse the string:
#    - Append each character to the corresponding row.
#    - Change direction when reaching:
#        • Top row (0)
#        • Bottom row (numRows - 1)
#    - Update curr_row accordingly.
# 4. Combine all rows:
#    - Join all row strings to get final result.

class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = list(nums)
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                ans[i] = max(ans[i], ans[stack.pop()])
            if stack:
                ans[stack[-1]] = max(ans[stack[-1]], ans[i])
            stack.append(i)
        
        for k in range(1, len(stack)):
            ans[stack[k-1]] = max(ans[stack[k-1]], ans[stack[k]])
        
        return ans
