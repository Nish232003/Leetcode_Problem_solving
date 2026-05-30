# LeetCode 54: Spiral Matrix | Boundary Traversal

# Approach:
# Instead of using extra visited arrays, we maintain four boundaries
# (top, bottom, left, right) and traverse layer by layer in spiral order.

# 1. Initialize:
#    - 'top' and 'bottom' for row boundaries.
#    - 'left' and 'right' for column boundaries.
#    - 'ans' list to store spiral traversal.

# 2. Traverse in 4 directions:
#    - Left → Right across top row
#    - Top → Bottom across right column
#    - Right → Left across bottom row
#    - Bottom → Top across left column

# 3. After each traversal:
#    - Shrink the corresponding boundary.

# 4. Continue until:
#    - top > bottom OR left > right

# 5. Complexity:
#    - Time Complexity: O(m * n)
#    - Space Complexity: O(1) excluding output array


class Solution:
    def spiralOrder(self, matrix):

        ans = []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:

            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans
