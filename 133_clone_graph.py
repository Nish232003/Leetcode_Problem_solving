# LeetCode 133: Clone Graph | DFS + Hash Map

# Approach:
# Instead of creating duplicate nodes multiple times, we use a hash map
# to store already cloned nodes and perform DFS traversal.

# 1. Handle edge case:
#    - If the graph is empty (node is None), return None.

# 2. Initialize:
#    - Create a dictionary 'mp' to map original nodes to cloned nodes.

# 3. DFS Traversal:
#    - If a node is already cloned, return the cloned node.
#    - Create a new node with the same value.
#    - Store it in the hash map.
#    - Recursively clone all neighbors and add them to the cloned node.

# 4. Return:
#    - Start DFS from the given node and return the cloned graph.

# 5. Complexity:
#    - Time Complexity: O(V + E)
#    - Space Complexity: O(V)


class Solution(object):
    def cloneGraph(self, node):

        if not node:
            return None

        mp = {}

        def dfs(curr):

            if curr in mp:
                return mp[curr]

            clone = Node(curr.val)
            mp[curr] = clone

            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
