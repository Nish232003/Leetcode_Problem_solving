# LeetCode 117: Populating Next Right Pointers in Each Node II | Level Order Linking (O(1) space)

# Approach:
# We connect nodes level by level using already established next pointers.
# No extra queue is used (constant extra space).

# 1. Use a dummy node for each level.
# 2. 'prev' tracks the last connected node in the next level.
# 3. Traverse current level using 'curr' and already built next pointers.
# 4. For each node:
#    - Connect its children to the next level chain.
# 5. Move to next level via dummy.next.

# 6. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)

class Solution(object):
    def connect(self, root):
        if not root:
            return root

        curr = root

        while curr:
            dummy = Node(0)
            prev = dummy

            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next

                if curr.right:
                    prev.next = curr.right
                    prev = prev.next

                curr = curr.next

            curr = dummy.next

        return root
