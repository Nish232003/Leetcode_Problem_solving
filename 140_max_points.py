# LeetCode 149: Max Points on a Line | Slope Counting with Hash Map

# Approach:
# For every point, treat it as the starting point and calculate slopes
# with all remaining points.

# 1. Handle edge case:
#    - If number of points is 2 or less, return n.

# 2. For each point i:
#    - Create a hash map to count occurrences of each slope.
#    - Compare point i with every point j > i.

# 3. Compute slope:
#    - dx = x2 - x1
#    - dy = y2 - y1
#    - Reduce (dy, dx) using gcd to avoid floating-point errors.
#    - Store normalized slope as a tuple.

# 4. Update slope frequency:
#    - Count how many points share the same slope with point i.

# 5. Track maximum points:
#    - The line through point i contains:
#         slope_count + 1
#      (+1 for the starting point itself).

# 6. Complexity:
#    - Time Complexity: O(n²)
#    - Space Complexity: O(n)


class Solution:
    def maxPoints(self, points):

        n = len(points)

        if n <= 2:
            return n

        from collections import defaultdict
        from math import gcd

        ans = 1

        for i in range(n):

            slopes = defaultdict(int)

            x1, y1 = points[i]

            for j in range(i + 1, n):

                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                g = gcd(dx, dy)

                dx //= g
                dy //= g

                if dx < 0:
                    dx *= -1
                    dy *= -1
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slopes[(dy, dx)] += 1

                ans = max(ans, slopes[(dy, dx)] + 1)

        return ans
