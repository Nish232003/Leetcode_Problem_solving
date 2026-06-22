# LeetCode 1840: Maximum Building Height | Greedy + Forward & Backward Pass

# Approach:
# Instead of assigning heights to every building, we process only the restricted
# buildings and propagate constraints in both directions.

# 1. Add boundary restrictions:
#    - Building 1 has height 0.
#    - Building n can have at most (n - 1) height due to adjacent difference ≤ 1.

# 2. Sort restrictions by building index.

# 3. Forward pass:
#    - Moving left to right, ensure each building's maximum height is achievable
#      from the previous restriction.
#    - height[i] ≤ height[i-1] + distance

# 4. Backward pass:
#    - Moving right to left, ensure each building's maximum height is achievable
#      from the next restriction.
#    - height[i] ≤ height[i+1] + distance

# 5. Find the maximum possible peak:
#    - Between two consecutive restrictions, the height can increase and then
#      decrease by at most 1 per building.
#    - Maximum peak =
#      (left_height + right_height + distance) // 2

# 6. Complexity:
#    - Time Complexity: O(m log m)
#      where m = number of restrictions
#    - Space Complexity: O(m)


class Solution(object):
    def maxBuilding(self, n, restrictions):

        restrictions.append([1, 0])
        restrictions.append([n, n - 1])

        restrictions.sort()

        m = len(restrictions)

        for i in range(1, m):
            d = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(restrictions[i][1],
                                     restrictions[i - 1][1] + d)

        for i in range(m - 2, -1, -1):
            d = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1],
                                     restrictions[i + 1][1] + d)

        ans = 0

        for i in range(1, m):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            d = x2 - x1

            ans = max(ans, (h1 + h2 + d) // 2)

        return ans
