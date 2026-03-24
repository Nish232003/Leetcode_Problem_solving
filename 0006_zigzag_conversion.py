# LeetCode 6: Zigzag Conversion | Simulation + Direction Tracking

# Approach:
# Instead of constructing the zigzag pattern in a matrix, we simulate the traversal
# row by row using a direction-based approach.

# 1. Handle edge case:
#    - If numRows == 1 or numRows >= len(s), return the original string.

# 2. Initialize:
#    - Create a list 'rows' to store characters for each row.
#    - Use 'curr_row' to track the current row.
#    - Use 'direction' to control movement (down = 1, up = -1).

# 3. Traverse the string:
#    - Append each character to the corresponding row.
#    - Change direction when reaching:
#        • Top row (0)
#        • Bottom row (numRows - 1)
#    - Update curr_row accordingly.

# 4. Combine all rows:
#    - Join all row strings to get final result.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


class Solution(object):
    def convert(self, s, numRows):

        
        if numRows == 1 or numRows >= len(s):
            return s

        
        rows = [""] * numRows

        curr_row = 0
        direction = 1  

        
        for char in s:
            rows[curr_row] += char

            
            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1

            curr_row += direction

        
        return "".join(rows)
