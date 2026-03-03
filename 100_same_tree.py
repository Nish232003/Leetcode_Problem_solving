# Leetcode : 100 Same Tree
# Leetcode link : https://leetcode.com/problems/same-tree/

# Approach :
# We compare both trees recursively.
# Two trees are same if:
# 1. Both nodes are None.
# 2. Both nodes have same value.
# 3. Left subtrees are same.
# 4. Right subtrees are same.

# Time Complexity : O(n)

# Space Complexity : O(h)

class Solution(object):
    def isSameTree(self, p, q):

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)
