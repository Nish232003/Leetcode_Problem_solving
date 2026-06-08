# LeetCode 74: Search a 2D Matrix | Binary Search on Virtual 1D Array

# Approach:
# Since:
# 1. Each row is sorted in non-decreasing order.
# 2. The first element of each row is greater than the last element
#    of the previous row.
#
# We can treat the entire matrix as a single sorted 1D array.
#
# 1. Initialize binary search on indices from 0 to (m * n - 1).
#
# 2. For each middle index:
#    - Convert it back to 2D coordinates:
#        • row = mid // n
#        • col = mid % n
#    - Access matrix[row][col].
#
# 3. Compare with target:
#    - If equal, return True.
#    - If smaller, search right half.
#    - If larger, search left half.
#
# 4. If target is not found, return False.
#
# 5. Complexity:
#    - Time Complexity: O(log(m * n))
#    - Space Complexity: O(1)


class Solution(object):
    def searchMatrix(self, matrix, target):

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:

            mid = (left + right) // 2

            row = mid // n
            col = mid % n

            value = matrix[row][col]

            if value == target:
                return True

            elif value < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
