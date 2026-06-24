# LeetCode 3699: Number of ZigZag Arrays I | Dynamic Programming + Prefix Sums

# Approach:
# Instead of storing the entire array, we only track the last element
# and the direction of the previous move.

# 1. Define DP states:
#    - up[x]   = number of valid arrays ending at value x where
#                the last step was increasing.
#    - down[x] = number of valid arrays ending at value x where
#                the last step was decreasing.

# 2. Initialize length = 2:
#    - For every pair (a, b):
#         a < b → contributes to up[b]
#         a > b → contributes to down[b]

# 3. Transition:
#    - To end at value x with an increasing step,
#      previous step must be decreasing and previous value < x.
#    - To end at value x with a decreasing step,
#      previous step must be increasing and previous value > x.
#    - Use prefix/suffix sums to compute these transitions efficiently.

# 4. Repeat until length n.

# 5. Final answer:
#    - Sum all up and down states.

# 6. Complexity:
#    - Time Complexity: O(n * m)
#    - Space Complexity: O(m)
#      where m = r - l + 1


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l + 1

        up = [0] * m
        down = [0] * m

        for x in range(m):
            up[x] = x
            down[x] = m - 1 - x

        for _ in range(3, n + 1):
            pref_down = [0] * (m + 1)
            pref_up = [0] * (m + 1)

            for i in range(m):
                pref_down[i + 1] = (pref_down[i] + down[i]) % MOD
                pref_up[i + 1] = (pref_up[i] + up[i]) % MOD

            total_up = pref_up[m]

            new_up = [0] * m
            new_down = [0] * m

            for x in range(m):
                new_up[x] = pref_down[x]
                new_down[x] = (total_up - pref_up[x + 1]) % MOD

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD
