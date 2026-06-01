# LeetCode 36: Valid Sudoku | HashSet Validation

# Approach:
# Instead of checking every row, column, and box separately multiple times,
# we use sets to track already seen numbers efficiently.

# 1. Initialize:
#    - Create 3 lists of sets:
#        • rows   -> tracks numbers in each row
#        • cols   -> tracks numbers in each column
#        • boxes  -> tracks numbers in each 3x3 sub-box

# 2. Traverse the board:
#    - Ignore empty cells ('.')
#    - Compute box index using:
#         (row // 3) * 3 + (col // 3)
#
# 3. Validation:
#    - If current number already exists in:
#         • current row
#         • current column
#         • current box
#      then Sudoku is invalid.

# 4. Otherwise:
#    - Add the number into corresponding row, column, and box sets.

# 5. Complexity:
#    - Time Complexity: O(9 × 9) = O(1)
#    - Space Complexity: O(1)


class Solution(object):
    def isValidSudoku(self, board):

        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        
        for i in range(9):
            for j in range(9):

                num = board[i][j]

                
                if num == ".":
                    continue

                
                box = (i // 3) * 3 + (j // 3)

                
                if num in rows[i] or num in cols[j] or num in boxes[box]:
                    return False

                
                rows[i].add(num)
                cols[j].add(num)
                boxes[box].add(num)

        
        return True
