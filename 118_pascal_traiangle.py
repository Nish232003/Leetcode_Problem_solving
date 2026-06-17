# LeetCode 118: Pascal's Triangle | Iterative Construction

# Approach:
# Each row is built from the previous row.
# Rule:
# - First and last element of each row is 1
# - Middle elements = sum of two elements above it

# 1. Start with first row [1]
# 2. For each next row:
#    - Build using previous row
# 3. Repeat until numRows

# 4. Complexity:
#    - Time Complexity: O(numRows^2)
#    - Space Complexity: O(numRows^2)

class Solution(object):
    def generate(self, numRows):
        res = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]

            res.append(row)

        return res
