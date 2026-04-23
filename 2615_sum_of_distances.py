

# LeetCode 2615: Sum of Distances | HashMap + Prefix Sum

# Approach:
# Instead of calculating distances using brute force (O(n^2)),
# we group indices of same values and compute distances efficiently.

# 1. Group Indices:
#    - Use hashmap to store all indices for each unique number.

# 2. Prefix Sum:
#    - For each group of indices, build prefix sum array.
#    - Helps compute sum of distances in constant time.

# 3. Distance Calculation:
#    - For each index:
#        Left contribution  = index * count_left - sum_left
#        Right contribution = sum_right - index * count_right
#    - Total distance = left + right

# 4. Edge Case:
#    - If an element appears only once → distance = 0

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)

# Clean Code:
# - Used meaningful variable names (indices, prefix, res)
# - Separated logic into clear steps (grouping, prefix, calculation)
# - Avoided redundant computations using prefix sums

from collections import defaultdict

class Solution(object):
    def distance(self, nums):
        positions = defaultdict(list)
        
        
        for i, num in enumerate(nums):
            positions[num].append(i)
        
        result = [0] * len(nums)
        
        
        for indices in positions.values():
            n = len(indices)
            
            
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i + 1] = prefix[i] + indices[i]
            
            
            for i in range(n):
                idx = indices[i]
                
                left = idx * i - prefix[i]
                right = (prefix[n] - prefix[i + 1]) - idx * (n - i - 1)
                
                result[idx] = left + right
        
        return result
