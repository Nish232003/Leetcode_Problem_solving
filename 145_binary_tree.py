# LeetCode 145: Binary Tree Postorder Traversal | Iterative DFS using Stack

# Approach:
# Postorder traversal follows:
#    Left -> Right -> Root
#
# We can obtain postorder by performing a modified preorder:
#    Root -> Right -> Left
#
# Then reverse the result at the end to get:
#    Left -> Right -> Root
#
# 1. Handle edge case:
#    - If root is None, return an empty list.
#
# 2. Initialize:
#    - Create an empty result list.
#    - Push root onto the stack.
#
# 3. Process nodes:
#    - Pop a node from the stack.
#    - Add its value to the result.
#    - Push its left child first.
#    - Push its right child second.
#
#    This produces:
#    Root -> Right -> Left
#
# 4. Reverse the result list.
#
# 5. Return the reversed result.
#
# 6. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


class Solution(object):
    def postorderTraversal(self, root):

        if not root:
            return []

        result = []
        stack = [root]

        while stack:

            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return result[::-1]
