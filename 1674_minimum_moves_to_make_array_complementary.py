# LeetCode 1674: Minimum Moves to Make Array Complementary | Difference Array + Prefix Sum

# Approach:
# Instead of checking every possible target sum separately, we use a
# difference array technique to efficiently track how many moves are needed
# for every possible pair sum.

# 1. Pair elements:
#    - Use two pointers:
#        • left from start
#        • right from end
#    - Each pair is:
#        nums[left] + nums[right]

# 2. Understand move ranges:
#    For every pair (a, b):
#
#    - 0 moves:
#        • When target sum = a + b
#
#    - 1 move:
#        • Possible in range:
#          [min(a,b)+1 , max(a,b)+limit]
#
#    - 2 moves:
#        • Needed for all other sums

# 3. Use difference array:
#    - Instead of updating every value individually,
#      update ranges efficiently using prefix sum logic.
#
#    - Initially assume every sum needs 2 moves.
#
#    - Reduce moves for:
#        • 1-move range
#        • Exact 0-move sum

# 4. Build prefix sum:
#    - Traverse all possible sums from 2 to 2*limit
#    - Accumulate moves using prefix sums
#    - Track minimum moves

# 5. Complexity:
#    - Time Complexity: O(n + limit)
#    - Space Complexity: O(limit)
class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        
        n = len(nums)
        
        # Difference array
        diff = [0] * (2 * limit + 2)
        
        left = 0
        right = n - 1
        
        while left < right:
            a = nums[left]
            b = nums[right]
            
            low = min(a, b) + 1
            high = max(a, b) + limit
            total = a + b
            
            # Initially every sum needs 2 moves
            diff[2] += 2
            
            # 1 move range
            diff[low] -= 1
            diff[high + 1] += 1
            
            # 0 move at exact sum
            diff[total] -= 1
            diff[total + 1] += 1
            
            left += 1
            right -= 1
        
        ans = float('inf')
        curr = 0
        
        for s in range(2, 2 * limit + 1):
            curr += diff[s]
            ans = min(ans, curr)
        
        return ans
