# LeetCode 1559: Detect Cycles in 2D Grid | DFS + Parent Tracking

# Approach:
# We treat the grid as a graph where each cell is a node.
# We use DFS to detect cycles in connected components of same-value cells.

# 1. Traverse each cell:
#    - For every unvisited cell, start a DFS.

# 2. DFS Traversal:
#    - Move in 4 directions: up, down, left, right.
#    - Only move to cells having the same value.

# 3. Track visited cells:
#    - Use a visited matrix to avoid reprocessing nodes.

# 4. Parent Tracking (Key Step):
#    - While moving, pass the parent cell coordinates.
#    - If we encounter a visited cell that is NOT the parent,
#      it means a cycle is detected.

# 5. Return result:
#    - If any DFS finds a cycle → return True.
#    - Otherwise → return False.

# 6. Complexity:
#    - Time Complexity: O(m * n)
#    - Space Complexity: O(m * n)


class Solution(object):
    def containsCycle(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c, pr, pc):
            visited[r][c] = True
            directions = [(0,1), (1,0), (0,-1), (-1,0)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r][c]:
                    
                    if not visited[nr][nc]:
                        if dfs(nr, nc, r, c):
                            return True
                    elif (nr, nc) != (pr, pc):
                        return True

            return False

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1):
                        return True

        return False
