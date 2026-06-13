# LeetCode 206: Reverse Linked List | Iterative Approach

# Approach:
# Instead of creating a new list, we reverse the links between nodes in-place.

# 1. Initialize:
#    - 'prev' as None (previous node).
#    - 'curr' as head (current node).

# 2. Traverse the linked list:
#    - Store the next node in 'nxt'.
#    - Reverse the current node's pointer:
#         curr.next = prev
#    - Move both pointers forward:
#         prev = curr
#         curr = nxt

# 3. Continue until curr becomes None.

# 4. Return:
#    - 'prev' will point to the new head of the reversed list.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def reverseList(self, head):

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

        return prev
