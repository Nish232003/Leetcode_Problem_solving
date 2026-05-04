#LeetCode 48: Rotate Image | In-place Transpose + Reverse

# Approach:
# To rotate the matrix 90° clockwise without using extra space,
# we perform two steps:

# 1. Transpose the matrix:
#    - Convert rows into columns (matrix[i][j] -> matrix[j][i])
#    - Swap only upper triangle to avoid double swapping

# 2. Reverse each row:
#    - This aligns elements to achieve clockwise rotation

# Time Complexity: O(n^2)
# Space Complexity: O(1)  (in-place)

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

  
        for i in range(n):
            for j in range(i, n):  
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

     
        for i in range(n):
            matrix[i].reverse()
