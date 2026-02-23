# Leetcode : 94. Binary Tree Inorder Traversal
# Leetcode link : https://leetcode.com/problems/binary-tree-inorder-traversal/

# Approach :
# The goal is to return the inorder traversal of a binary tree.
# In inorder traversal we visit nodes in the order:
# Left subtree → Root → Right subtree

# Time complexity : O(n)
# Space complexity : O(h)  (h = height of tree)

# Steps :
# 1. Start from root node.
# 2. Traverse left subtree first.
# 3. Visit the current node and store its value.
# 4. Traverse right subtree.
# 5. Continue until all nodes are visited.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


