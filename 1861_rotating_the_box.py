# LeetCode 1861 - Rotating the Box

#- Simulated gravity for stones before rotation
#- Handled obstacles while shifting stones
#- Added 90-degree clockwise matrix rotation
#- Optimized solution using two-pointer approach
#- Improved readability and time efficiency

class Solution(object):
    def rotateTheBox(self, boxGrid):
        rows = len(boxGrid)
        cols = len(boxGrid[0])

        for r in range(rows):
            empty = cols - 1

            for c in range(cols - 1, -1, -1):

                if boxGrid[r][c] == '*':
                    empty = c - 1

                elif boxGrid[r][c] == '#':
                    boxGrid[r][c] = '.'
                    boxGrid[r][empty] = '#'
                    empty -= 1

        ans = [[None] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                ans[c][rows - 1 - r] = boxGrid[r][c]

        return ans
