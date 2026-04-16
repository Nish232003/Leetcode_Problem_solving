# LeetCode: 3488. Closest Equal Element Queries

# Approach:
# - Use a hashmap to store indices of each number.
# - For each query, find all positions of the queried value.
# - Use binary search to locate the closest index.
# - Check left and right neighbors for minimum distance.
# - Compute circular distance using min(abs(i-j), n - abs(i-j)).

import bisect
from collections import defaultdict

class Solution(object):
    def solveQueries(self, nums, queries):
        pos = defaultdict(list)
        n = len(nums)
        
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        result = []
        
        for q in queries:
            val = nums[q]
            indices = pos[val]
            
            if len(indices) == 1:
                result.append(-1)
                continue
            
            i = bisect.bisect_left(indices, q)
            
            left = indices[i - 1] if i > 0 else indices[-1]
            right = indices[i + 1] if i < len(indices) - 1 else indices[0]
            
            d1 = min(abs(q - left), n - abs(q - left))
            d2 = min(abs(q - right), n - abs(q - right))
            
            result.append(min(d1, d2))
        
        return result
