# LeetCode 130: Surrounded Regions | DFS from Boundary

# Approach:
# A region should NOT be captured if it is connected
# to any 'O' on the board boundary.
#
# 1. Traverse all boundary cells.
#    - Whenever an 'O' is found, run DFS.
#    - Mark all connected 'O' cells as '#'.
#
# 2. After marking:
#    - Remaining 'O' cells are surrounded,
#      so convert them to 'X'.
#    - Convert '#' back to 'O' because these
#      cells are connected to the boundary.
#
# Example:
#
# X X X X
# X O O X
# X X O X
# X O X X
#
# Boundary DFS marks the bottom 'O':
#
# X X X X
# X O O X
# X X O X
# X # X X
#
# Convert:
# O -> X
# # -> O
#
# Result:
#
# X X X X
# X X X X
# X X X X
# X O X X
#
# Complexity:
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)   (DFS recursion stack)


class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if board[r][c] != 'O':
                return

            board[r][c] = '#'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
