# LeetCode 147: Insertion Sort List | Linked List Insertion Sort

# Approach:
# We build a new sorted linked list using the insertion sort technique.
#
# 1. Create a dummy node before the sorted list.
#
# 2. Traverse the original list one node at a time.
#
# 3. For each node:
#    - Find its correct position in the sorted part.
#    - Insert it between two nodes.
#
# 4. Continue until all nodes are processed.
#
# 5. Return dummy.next as the head of the sorted list.
#
# 6. Complexity:
#    - Time Complexity: O(n²)
#      (For each node, we may traverse the sorted part.)
#    - Space Complexity: O(1)
#      (Sorting is done in-place.)


class Solution(object):
    def insertionSortList(self, head):

        dummy = ListNode(0)
        curr = head

        while curr:

            prev = dummy
            nxt = curr.next

            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            curr.next = prev.next
            prev.next = curr

            curr = nxt

        return dummy.next
