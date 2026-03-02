# LeetCode 83 - Remove Duplicates from Sorted List
# Approach: Traverse the sorted linked list and remove adjacent duplicates
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
