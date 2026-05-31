# LeetCode 59: Spiral Matrix II | Boundary Traversal

# Approach:
# We generate the matrix layer by layer using four boundaries:
#    - top
#    - bottom
#    - left
#    - right
#
# Fill numbers from 1 to n^2 in spiral order.

# 1. Initialize:
#    - Create an n x n matrix filled with 0.
#    - Set boundaries:
#         • top = 0
#         • bottom = n - 1
#         • left = 0
#         • right = n - 1
#    - Start filling number from 1.

# 2. Traverse in 4 directions:
#    - Left → Right
#    - Top → Bottom
#    - Right → Left
#    - Bottom → Top
#
# After each traversal, shrink the corresponding boundary.

# 3. Continue until all layers are filled.

# 4. Complexity:
#    - Time Complexity: O(n^2)
#    - Space Complexity: O(n^2)


class Solution(object):
    def generateMatrix(self, n):

        
        matrix = [[0] * n for _ in range(n)]

        
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        num = 1

        
        while top <= bottom and left <= right:

            
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1

            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1

        
        return matrix
