# LeetCode 24: Swap Nodes in Pairs | Linked List | Pointer Manipulation

# Approach:
# Instead of modifying node values, we swap nodes by changing links.

# 1. Handle edge case:
#    - If head is None or head.next is None, return head.

# 2. Initialize:
#    - Create a dummy node pointing to head.
#    - Use 'prev' to track node before the pair.

# 3. Traverse the list:
#    - Pick nodes in pairs:
#         first = prev.next
#         second = prev.next.next
#
#    - Swap nodes:
#         first.next = second.next
#         second.next = first
#         prev.next = second
#
#    - Move prev to next pair.

# 4. Return result:
#    - Return dummy.next.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def swapPairs(self, head):

        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

        return dummy.next
