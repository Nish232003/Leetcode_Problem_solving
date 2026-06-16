# LeetCode 82: Remove Duplicates from Sorted List II | Dummy Node + Two Pointers

# Approach:
# Since the linked list is sorted, duplicates appear consecutively.
# We need to remove ALL nodes that have duplicate values (not just keep one).

# 1. Use a dummy node:
#    - Helps handle cases where head itself must be removed.

# 2. Use a pointer 'prev':
#    - Tracks last node confirmed to be part of the result list.

# 3. Traverse with 'curr':
#    - If curr starts a duplicate sequence:
#        • skip all nodes with same value
#        • connect prev.next to the first non-duplicate node
#    - Else:
#        • move prev forward

# 4. Return dummy.next as new head.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)

class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next

            curr = curr.next

        return dummy.next
