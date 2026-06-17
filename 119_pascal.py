# LeetCode 119: Pascal's Triangle II | O(k) Space Optimization

# Approach:
# We generate only one row iteratively instead of building full triangle.

# Key idea:
# - Start with [1]
# - Each new row is built from previous row
# - Update from right to left to avoid overwriting values

# 1. Initialize result = [1]
# 2. For each row from 1 to rowIndex:
#    - Append 1 at end
#    - Update middle elements from right to left

# 3. Complexity:
#    - Time Complexity: O(rowIndex^2)
#    - Space Complexity: O(rowIndex)

class Solution(object):
    def getRow(self, rowIndex):
        res = [1]

        for i in range(1, rowIndex + 1):
            res.append(1)
            for j in range(i - 1, 0, -1):
                res[j] = res[j] + res[j - 1]

        return res
