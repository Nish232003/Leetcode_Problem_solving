# LeetCode 117: Populating Next Right Pointers in Each Node II | Level Order Linking with O(1) Space

# Approach:
# Unlike LeetCode 116, this tree is not necessarily perfect.
# We connect nodes level by level using already established next pointers.

# 1. Handle edge case:
#    - If root is None, return root.

# 2. Traverse each level:
#    - 'curr' points to nodes in the current level.
#    - Use a dummy node to build the next level's linked list.
#    - 'tail' always points to the last connected node in the next level.

# 3. For every node:
#    - If left child exists, connect it to tail.
#    - If right child exists, connect it to tail.
#    - Move curr using curr.next.

# 4. Move to next level:
#    - After finishing current level, start from dummy.next.

# 5. Repeat until no more levels remain.

# 6. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        curr = root

        while curr:

            dummy = Node(0)
            tail = dummy

            while curr:

                if curr.left:
                    tail.next = curr.left
                    tail = tail.next

                if curr.right:
                    tail.next = curr.right
                    tail = tail.next

                curr = curr.next

            curr = dummy.next

        return root
