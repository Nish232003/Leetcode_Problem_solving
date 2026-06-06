# LeetCode 73: Set Matrix Zeroes
# Constant Space Solution

# Approach:
# We must set the entire row and column to 0 if any cell contains 0.
#
# To achieve O(1) extra space:
#
# 1. Use the first row and first column as markers.
#
# 2. First pass:
#    - If matrix[i][j] == 0:
#      • Mark its row using matrix[i][0]
#      • Mark its column using matrix[0][j]
#
# 3. Keep separate flags for:
#    - Whether first row originally contains a zero.
#    - Whether first column originally contains a zero.
#
# 4. Second pass:
#    - For every cell except first row/column:
#      If its row or column is marked,
#      set it to 0.
#
# 5. Finally:
#    - Zero out the first row if needed.
#    - Zero out the first column if needed.
#
# Complexity:
# - Time Complexity: O(m * n)
# - Space Complexity: O(1)


class Solution(object):
    def setZeroes(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        for i in range(1, rows):
            for j in range(1, cols):

                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):

                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
