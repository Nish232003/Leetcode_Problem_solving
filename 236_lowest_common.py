# LeetCode 236: Lowest Common Ancestor of a Binary Tree | DFS + Recursion

# Approach:
# Instead of storing parent pointers or paths, we use DFS to search for p and q
# in the left and right subtrees and determine the first node where both are found.

# 1. Base Case:
#    - If the current node is None, return None.
#    - If the current node is either p or q, return the current node.

# 2. Search both subtrees:
#    - Recursively search the left subtree.
#    - Recursively search the right subtree.

# 3. Determine the LCA:
#    - If both left and right recursive calls return non-null values,
#      it means p and q are found in different subtrees, so the current
#      node is their Lowest Common Ancestor.
#    - If only one side returns a node, propagate that node upward.
#    - If neither side contains p or q, return None.

# 4. Start DFS from the root and return the result.

# 5. Complexity:
#    - Time Complexity: O(n)
#      Each node is visited once.
#    - Space Complexity: O(h)
#      where h is the height of the tree (O(log n) for balanced trees,
#      O(n) in the worst case).


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right
