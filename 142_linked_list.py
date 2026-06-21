# LeetCode 142: Linked List Cycle II | Floyd's Cycle Detection

# Approach:
# We use Floyd's Tortoise and Hare algorithm to detect a cycle and find
# the node where the cycle begins.

# 1. Initialize two pointers:
#    - slow moves one step at a time.
#    - fast moves two steps at a time.

# 2. Detect cycle:
#    - If slow and fast meet, a cycle exists.
#    - If fast reaches null, there is no cycle.

# 3. Find the starting node of the cycle:
#    - Place one pointer at head.
#    - Keep the other pointer at the meeting point.
#    - Move both pointers one step at a time.
#    - Their meeting point is the starting node of the cycle.

# 4. Return the node where the cycle starts.

# 5. Complexity:
#    - Time Complexity: O(N)
#    - Space Complexity: O(1)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):

        slow = fast = head

        # Detect cycle
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                # Find cycle start
                ptr = head

                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next

                return ptr

        return None
