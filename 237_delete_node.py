# LeetCode 237: Delete Node in a Linked List | Value Copy + Pointer Update

# Approach:
# Since we are not given access to the head of the linked list and the node
# to be deleted is guaranteed not to be the last node, we cannot remove it
# directly. Instead, we overwrite its value with the next node's value and
# bypass the next node.

# 1. Copy the value of the next node into the current node.
#    - node.val = node.next.val

# 2. Skip the next node by updating the next pointer.
#    - node.next = node.next.next

# 3. This effectively removes the next node and makes the current node
#    represent its successor.

# 4. Complexity:
#    - Time Complexity: O(1)
#      Only constant-time operations are performed.
#    - Space Complexity: O(1)
#      No extra space is used.


class Solution(object):
    def deleteNode(self, node):

        node.val = node.next.val
        node.next = node.next.next
