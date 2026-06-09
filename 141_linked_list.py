# LeetCode 141: Linked List Cycle | Floyd's Cycle Detection Algorithm

# Approach:
# We use two pointers:
#    - slow moves one step at a time.
#    - fast moves two steps at a time.
#
# 1. Initialize both pointers at the head.
#
# 2. Traverse the linked list:
#    - Move slow by one node.
#    - Move fast by two nodes.
#
# 3. If a cycle exists:
#    - The fast pointer will eventually catch up to the slow pointer.
#    - Return True.
#
# 4. If fast reaches the end of the list:
#    - No cycle exists.
#    - Return False.
#
# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def hasCycle(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
