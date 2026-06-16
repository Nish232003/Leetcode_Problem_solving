# LeetCode 85: Maximal Rectangle | Histogram Reduction + Stack

# Approach:
# Convert each row into a histogram where:
#   height[j] = number of consecutive '1's above (including current row)
#
# Then, for each row, compute Largest Rectangle in Histogram (LeetCode 84).

# 1. Maintain a height array:
#    - Update heights row by row.

# 2. For each row:
#    - Treat heights as histogram
#    - Compute max rectangle using monotonic stack

# 3. Complexity:
#    - Time Complexity: O(rows * cols)
#    - Space Complexity: O(cols)

class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0

            stack = []
            for i in range(cols + 1):
                curr_height = heights[i] if i < cols else 0

                while stack and curr_height < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    max_area = max(max_area, h * width)

                stack.append(i)

        return max_area
