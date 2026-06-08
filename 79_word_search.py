# LeetCode 79: Word Search | Backtracking + DFS

# Approach:
# We need to determine whether the given word can be formed
# by sequentially adjacent cells in the board.
#
# Rules:
# - We can move only in 4 directions:
#     • Up
#     • Down
#     • Left
#     • Right
# - A cell can be used only once in a single path.
#
# We use DFS + Backtracking:
#
# 1. Start DFS from every cell in the board.
#
# 2. For each DFS call:
#    - If all characters of the word are matched,
#      return True.
#    - If the current cell is invalid or does not match
#      the required character, return False.
#
# 3. Mark the current cell as visited.
#
# 4. Explore all 4 directions recursively.
#
# 5. Restore the original value of the cell
#    (Backtracking) before returning.
#
# 6. If any DFS path forms the complete word,
#    return True.
#
# 7. If all starting positions fail,
#    return False.
#
# 8. Complexity:
#    - Time Complexity: O(m * n * 4^L)
#      where L = length of word
#    - Space Complexity: O(L)
#      (Recursion stack)


class Solution(object):
    def exist(self, board, word):

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):

            if index == len(word):
                return True

            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[index]):
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):

                if dfs(r, c, 0):
                    return True

        return False
