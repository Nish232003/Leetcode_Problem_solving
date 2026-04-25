# Approach:
# We convert all boundary points of the square into a 1D circular representation
# (perimeter of the square), then apply binary search on the answer.

# 1. Convert 2D → 1D (Perimeter Mapping):
#    - Map each (x, y) to a position along the square boundary in clockwise order
#    - This reduces the problem to selecting points on a circular line

# 2. Sort + Extend:
#    - Sort perimeter positions
#    - Duplicate array with +perimeter to handle circular wrap-around

# 3. Binary Search on Minimum Distance:
#    - Search for the largest minimum Manhattan distance (d)

# 4. Greedy Feasibility Check:
#    - Start from each point
#    - Use binary search (bisect) to jump to next valid point ≥ d away
#    - Repeat until k points are selected or fail
#    - Finally, validate circular wrap-around distance

# 5. Key Insight:
#    - Manhattan distance on square boundary behaves like circular arc distance
#    - So we use min(arc, total - arc) for correct validation

# 6. Complexity:
#    - Time: O(n log n + n log n log side)
#    - Space: O(n)


import bisect

class Solution:
    def maxDistance(self, side, points, k):
        
        def to_perim(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 2 * side + (side - x)
            else:
                return 3 * side + (side - y)
        
        perim = sorted(to_perim(x, y) for x, y in points)
        n = len(perim)
        total = 4 * side
        doubled = perim + [p + total for p in perim]
        
        def mdist(a, b):
            arc = (b - a) % total
            return min(arc, total - arc)
        
        def feasible(d):
            for s in range(n):
                cnt = 1
                cur = doubled[s]
                pos = s
                ok = True
                for _ in range(k - 1):
                    nxt = bisect.bisect_left(doubled, cur + d, pos + 1, s + n)
                    if nxt >= s + n:
                        ok = False
                        break
                    cur = doubled[nxt]
                    pos = nxt
                    cnt += 1
                if ok and cnt == k and mdist(perim[s], cur) >= d:
                    return True
            return False
        
        lo, hi, ans = 1, 2 * side, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
