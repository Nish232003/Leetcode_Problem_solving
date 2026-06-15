# LeetCode 51: N-Queens | Backtracking

# Approach:
# We place queens row by row using backtracking.
#
# Rules:
#    Two queens cannot share:
#       • Same column
#       • Same main diagonal (row - col)
#       • Same anti-diagonal (row + col)
#
# 1. Maintain:
#    - cols      -> occupied columns
#    - diag1     -> occupied main diagonals (row - col)
#    - diag2     -> occupied anti-diagonals (row + col)
#
# 2. For each row:
#    - Try placing a queen in every column.
#    - Skip positions that are under attack.
#    - Place queen and mark column/diagonals.
#    - Recurse for next row.
#    - Backtrack after returning.
#
# 3. Base Case:
#    - If all rows are processed,
#      store the current board configuration.
#
# 4. Complexity:
#    - Time Complexity: O(N!)
#    - Space Complexity: O(N)


class Solution(object):
    def solveNQueens(self, n):

        result = []

        board = [['.'] * n for _ in range(n)]

        cols = set()
        diag1 = set()     # row - col
        diag2 = set()     # row + col

        def backtrack(row):

            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):

                if (col in cols or
                    row - col in diag1 or
                    row + col in diag2):
                    continue

                board[row][col] = 'Q'

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                board[row][col] = '.'

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return result
