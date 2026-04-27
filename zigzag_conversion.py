# LeetCode 6: Zigzag Conversion

## Approach
#- Avoid constructing a 2D matrix; instead simulate zigzag traversal.
#- Use a list of strings (`rows`) to represent each row.
#- Maintain:
#  - `curr_row` → current row index
#  - `direction` → movement control (+1 for down, -1 for up)
#- Iterate through the string:
#  - Append each character to its respective row.
#  - Change direction when:
#    - At the top row (0)
#    - At the bottom row (numRows - 1)
#- Combine all rows to form the final result.

## Edge Cases
#- If `numRows == 1` or `numRows >= len(s)`, return the original string.

from collections import deque

class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        # Directions mapping: (dx, dy)
        directions = {
            1: [(0, -1), (0, 1)],     # left, right
            2: [(-1, 0), (1, 0)],     # up, down
            3: [(0, -1), (1, 0)],     # left, down
            4: [(0, 1), (1, 0)],      # right, down
            5: [(0, -1), (-1, 0)],    # left, up
            6: [(0, 1), (-1, 0)]      # right, up
        }

        # Opposite direction check
        def is_connected(d1, d2):
            return d1[0] + d2[0] == 0 and d1[1] + d2[1] == 0

        visited = [[False]*n for _ in range(m)]
        queue = deque([(0, 0)])
        visited[0][0] = True

        while queue:
            x, y = queue.popleft()

            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in directions[grid[x][y]]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # Check if next cell connects back
                    for back_dx, back_dy in directions[grid[nx][ny]]:
                        if is_connected((dx, dy), (back_dx, back_dy)):
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            break

        return False
