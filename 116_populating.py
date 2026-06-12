# LeetCode 116: Populating Next Right Pointers in Each Node | Level Connection Using Existing Next Pointers

# Approach:
# Since the tree is a perfect binary tree, every parent has exactly two children.
# We use already established next pointers to connect nodes level by level.

# 1. Handle edge case:
#    - If root is None, return root.

# 2. Start from the leftmost node of each level.
#    - 'leftmost' tracks the first node of the current level.

# 3. Traverse current level:
#    - Connect left child to right child.
#    - If current node has a next node, connect current's right child
#      to next node's left child.

# 4. Move to next level:
#    - Since it is a perfect binary tree, the leftmost node of the next
#      level is always leftmost.left.

# 5. Repeat until reaching the leaf level.

# 6. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        leftmost = root

        while leftmost.left:

            curr = leftmost

            while curr:

                curr.left.next = curr.right

                if curr.next:
                    curr.right.next = curr.next.left

                curr = curr.next

            leftmost = leftmost.left

        return root
