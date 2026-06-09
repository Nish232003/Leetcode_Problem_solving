# LeetCode 148: Sort List | Merge Sort on Linked List

# Approach:
# Since linked lists do not allow efficient random access,
# Merge Sort is the optimal sorting algorithm.
#
# 1. Base Case:
#    - If the list is empty or contains only one node,
#      it is already sorted.
#
# 2. Find the middle of the list:
#    - Use slow and fast pointers.
#    - Split the list into two halves.
#
# 3. Recursively sort both halves.
#
# 4. Merge the two sorted halves:
#    - Compare nodes from both lists.
#    - Attach the smaller node to the result list.
#
# 5. Return the merged sorted list.
#
# 6. Complexity:
#    - Time Complexity: O(n log n)
#    - Space Complexity: O(log n)
#      (Recursive call stack)


class Solution(object):
    def sortList(self, head):

        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(self, l1, l2):

        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:

            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        tail.next = l1 if l1 else l2

        return dummy.next
