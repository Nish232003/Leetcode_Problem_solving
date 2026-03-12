##Solved LeetCode 99 - Recover Binary Search Tree.
##Approach:
##Used inorder traversal to detect two misplaced nodes in the BST.
##Since inorder traversal of a BST should be sorted, any violation 
##(prev.val > curr.val) indicates swapped nodes.

class Solution(object):
    def recoverTree(self, root):
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            if self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            
            self.prev = node
            
            inorder(node.right)
        
        inorder(root)
        
        self.first.val, self.second.val = self.second.val, self.first.val
