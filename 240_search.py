# LeetCode 240: Search a 2D Matrix II | Top-Right Traversal

# Approach:
# Since each row is sorted left-to-right and each column is sorted top-to-bottom,
# we start from the top-right corner and eliminate one row or one column at each step.

# 1. Initialize:
#    - Start at the top-right element:
#        • row = 0
#        • col = n - 1

# 2. Traverse the matrix:
#    - While row is within bounds and col is within bounds:
#        • If matrix[row][col] == target, return True.
#        • If matrix[row][col] > target:
#              Move left (col -= 1), since everything below is even larger.
#        • If matrix[row][col] < target:
#              Move down (row += 1), since everything to the left is smaller.

# 3. If traversal ends without finding the target:
#    - Return False.

# 4. Complexity:
#    - Time Complexity: O(m + n)
#      At most one pass through rows and columns.
#    - Space Complexity: O(1)
#      No extra space is used.


class Solution(object):
    def searchMatrix(self, matrix, target):

        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols - 1

        while row < rows and col >= 0:

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                col -= 1

            else:
                row += 1

        return False
