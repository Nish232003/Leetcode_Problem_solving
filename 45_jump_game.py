# LeetCode 45: Jump Game II | Greedy + Range Tracking

# Approach:
# Instead of checking all possible jumps recursively, we greedily track
# the farthest position reachable within the current jump range.

# 1. Initialize:
#    - 'jumps' to count minimum jumps.
#    - 'end' to mark the current jump boundary.
#    - 'farthest' to store the farthest reachable index.

# 2. Traverse the array:
#    - Update 'farthest' using:
#         max(farthest, i + nums[i])
#    - When we reach the current boundary ('end'):
#         • Increment jumps
#         • Update end = farthest
#    - This means we start a new jump range.

# 3. Stop before the last index:
#    - No need to jump from the final position.

# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def jump(self, nums):

        jumps = 0
        end = 0
        farthest = 0

        
        for i in range(len(nums) - 1):

            farthest = max(farthest, i + nums[i])

            
            if i == end:
                jumps += 1
                end = farthest

        
        return jumps
