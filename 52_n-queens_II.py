# LeetCode 52: N-Queens II | Backtracking + Sets

# Approach:
# Instead of generating all board configurations, we directly count
# valid queen placements using backtracking.

# 1. Track occupied positions:
#    - 'cols' stores used columns.
#    - 'diag1' stores main diagonals (row - col).
#    - 'diag2' stores anti-diagonals (row + col).

# 2. Backtracking:
#    - Try placing a queen row by row.
#    - For each column:
#        • Skip if column or diagonal is already occupied.
#        • Otherwise place queen and move to next row.

# 3. Base Case:
#    - If all rows are filled, one valid arrangement is found.
#    - Return 1.

# 4. Backtrack:
#    - Remove the queen after recursive call
#      to explore other possibilities.

# 5. Complexity:
#    - Time Complexity: O(N!)
#    - Space Complexity: O(N)


class Solution(object):
    def totalNQueens(self, n):

        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row):

            if row == n:
                return 1

            count = 0

            for col in range(n):

                if (col in cols or
                    (row - col) in diag1 or
                    (row + col) in diag2):
                    continue

                
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                
                count += backtrack(row + 1)

                
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

            return count

        return backtrack(0)
