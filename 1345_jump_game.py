# LeetCode 1345: Jump Game IV | BFS + HashMap Optimization

# Approach:
# Instead of trying all possible paths recursively, we use Breadth-First Search (BFS)
# because BFS guarantees the minimum number of jumps in an unweighted graph.

# 1. Handle edge case:
#    - If array contains only one element, return 0 since we're already at the last index.

# 2. Build adjacency mapping:
#    - Use a hashmap (dictionary) where:
#          value -> list of indices having that value
#    - This helps us quickly jump to all same-value positions.

# 3. Initialize BFS:
#    - Start BFS from index 0.
#    - Use:
#         • queue -> for level-order traversal
#         • visited -> to avoid revisiting indices
#         • steps -> stores number of jumps

# 4. Process neighbors:
#    From current index, we can move to:
#       • index - 1
#       • index + 1
#       • all indices with same value
#
#    - Add valid unvisited neighbors into queue.

# 5. Important Optimization:
#    - After processing all indices of a value once,
#      clear that list from hashmap.
#    - Prevents repeated traversal and avoids TLE.

# 6. BFS Guarantee:
#    - First time we reach last index = minimum jumps.

# 7. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


from collections import defaultdict, deque


class Solution(object):

    def minJumps(self, arr):

        n = len(arr)

        
        if n == 1:
            return 0

        
        positions = defaultdict(list)

        for i, value in enumerate(arr):
            positions[value].append(i)

        
        queue = deque([0])
        visited = {0}
        steps = 0

        
        while queue:

            for _ in range(len(queue)):

                index = queue.popleft()

                
                if index == n - 1:
                    return steps

                
                neighbors = positions[arr[index]] + [index - 1, index + 1]

                
                for nxt in neighbors:

                    if 0 <= nxt < n and nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

                
                positions[arr[index]] = []

            
            steps += 1

        
        return -1
