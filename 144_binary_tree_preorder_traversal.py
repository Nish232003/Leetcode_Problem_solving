# LeetCode 144: Binary Tree Preorder Traversal | Iterative DFS using Stack

# Approach:
# Preorder traversal follows:
#    Root -> Left -> Right
#
# Instead of recursion, we use a stack.
#
# 1. Handle edge case:
#    - If root is None, return an empty list.
#
# 2. Initialize:
#    - Create an empty result list.
#    - Push root onto the stack.
#
# 3. Process nodes:
#    - Pop the top node from the stack.
#    - Add its value to the result.
#    - Push its right child first.
#    - Push its left child second.
#
#    Since stack is LIFO,
#    left child gets processed before right child.
#
# 4. Continue until stack becomes empty.
#
# 5. Return the result list.
#
# 6. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


class Solution(object):
    def preorderTraversal(self, root):

        if not root:
            return []

        result = []
        stack = [root]

        while stack:

            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result
