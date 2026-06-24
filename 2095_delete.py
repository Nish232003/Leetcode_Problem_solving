# LeetCode 2095: Delete the Middle Node of a Linked List | Fast & Slow Pointers

# Approach:
# Use two pointers to locate the middle node in one traversal.
#
# 1. Handle edge case:
#    - If the list contains only one node, return None.
#
# 2. Initialize:
#    - slow = head
#    - fast = head
#    - prev = None
#
# 3. Move pointers:
#    - slow moves one step at a time.
#    - fast moves two steps at a time.
#    - Keep track of the node before slow using prev.
#
# 4. When fast reaches the end:
#    - slow points to the middle node.
#    - Remove it by setting:
#          prev.next = slow.next
#
# 5. Return the modified head.
#
# 6. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution:
    def deleteMiddle(self, head):
        if not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head
