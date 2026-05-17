# LeetCode 1306: Jump Game III | DFS + Visited Set

# Approach:
# Treat each index as a node in a graph.
# From index i, we can jump:
#    • Forward  -> i + arr[i]
#    • Backward -> i - arr[i]
#
# We use DFS to explore all reachable indices.
# A visited set is used to avoid infinite loops.

# 1. Base Cases:
#    - If index goes out of bounds → return False
#    - If index is already visited → return False
#    - If arr[index] == 0 → return True

# 2. Mark current index as visited.

# 3. Recursively explore:
#    • Forward jump
#    • Backward jump

# 4. If either path reaches a 0, return True.

# 5. Complexity:
#    - Time Complexity: O(n)
#      (Each index is visited at most once)
#
#    - Space Complexity: O(n)
#      (Visited set + recursion stack)


class Solution(object):
    def canReach(self, arr, start):

        visited = set()

        def dfs(index):


            if index < 0 or index >= len(arr) or index in visited:
                return False


            if arr[index] == 0:
                return True


            visited.add(index)


            forward = dfs(index + arr[index])
            backward = dfs(index - arr[index])

            return forward or backward

        return dfs(start)
