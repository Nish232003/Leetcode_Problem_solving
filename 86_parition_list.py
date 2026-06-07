# LeetCode 86: Partition List | Two Dummy Linked Lists

# Approach:
# We create two separate linked lists:
#
# 1. "before" list:
#    - Stores nodes with values less than x.
#
# 2. "after" list:
#    - Stores nodes with values greater than or equal to x.
#
# While traversing the original list:
#    - Append each node to the appropriate list.
#
# After traversal:
#    - Connect the end of the "before" list
#      to the beginning of the "after" list.
#    - Set the last node of the "after" list to None
#      to avoid cycles.
#
# Since nodes are added in their original order,
# the relative ordering is preserved.

# 3. Return:
#    - Head of the "before" list.

# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)
#      (Only a few extra pointers are used)


class Solution(object):
    def partition(self, head, x):

        before_head = ListNode(0)
        after_head = ListNode(0)

        before = before_head
        after = after_head

        current = head

        while current:

            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next

            current = current.next

        after.next = None
        before.next = after_head.next

        return before_head.next
