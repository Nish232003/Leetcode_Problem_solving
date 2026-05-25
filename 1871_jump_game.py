# LeetCode 1871: Jump Game VII | BFS + Sliding Window

# Approach:
# Instead of checking every possible jump repeatedly, we use BFS traversal
# with an optimization using a sliding window technique.

# 1. Start from index 0:
#    - We can only move to positions containing '0'.
#    - Use a queue to store reachable indices.

# 2. Optimize repeated checking:
#    - Maintain a variable 'farthest' to track the farthest index
#      already processed.
#    - This prevents revisiting the same range multiple times.

# 3. BFS Traversal:
#    - For each reachable index:
#        • Explore indices from:
#              i + minJump
#          to:
#              i + maxJump
#        • Only process new indices beyond 'farthest'.

# 4. Valid move condition:
#    - s[j] == '0'
#    - If we reach the last index, return True.

# 5. If traversal finishes without reaching the end:
#    - Return False.

# 6. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


class Solution(object):
    def canReach(self, s, minJump, maxJump):

        n = len(s)

        
        queue = [0]

        
        farthest = 0

        
        for i in queue:

            
            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump, n - 1)

            
            for j in range(start, end + 1):

                
                if s[j] == '0':

                    
                    if j == n - 1:
                        return True

                    
                    queue.append(j)

            
            farthest = end

        
        return n == 1
