# LeetCode 37: Sudoku Solver | Optimized Backtracking + HashSets

# Approach:
# Instead of checking entire row, column, and box every time,
# we store existing numbers in sets for O(1) validation.

# 1. Initialize:
#    - rows[i]  -> numbers present in row i
#    - cols[j]  -> numbers present in column j
#    - boxes[k] -> numbers present in 3x3 box k
#
# 2. Store all empty cells separately.
#
# 3. Backtracking:
#    - Try digits 1 to 9 for each empty cell.
#    - If valid:
#         • Place digit
#         • Add to sets
#         • Recurse
#
# 4. Backtrack:
#    - Remove digit from board and sets if solution fails.
#
# 5. Complexity:
#    - Much faster than brute force validation.


class Solution(object):

    def solveSudoku(self, board):

        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        
        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    empty.append((i, j))

                else:
                    num = board[i][j]

                    rows[i].add(num)
                    cols[j].add(num)

                    box = (i // 3) * 3 + (j // 3)
                    boxes[box].add(num)

        
        def solve(idx):

            
            if idx == len(empty):
                return True

            row, col = empty[idx]

            box = (row // 3) * 3 + (col // 3)

            
            for num in "123456789":

                
                if num not in rows[row] and \
                   num not in cols[col] and \
                   num not in boxes[box]:

                    
                    board[row][col] = num

                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)

                    
                    if solve(idx + 1):
                        return True

                    
                    board[row][col] = "."

                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box].remove(num)

            
            return False

        
        solve(0)
