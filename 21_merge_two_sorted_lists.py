# Leetcode : 21. Merge Two Sorted Lists
# Leetcode link : https://leetcode.com/problems/merge-two-sorted-lists/

# Approach :
# The goal is to merge two already sorted linked lists into one sorted linked list.
# We compare nodes from both lists and attach the smaller node to the result list.
# Use a dummy node to simplify handling the head of the merged list.
#
# Time complexity : O(n + m)
# Space complexity : O(1)   (no extra space, only pointer manipulation)

# Steps :
# 1. Create a dummy node to act as the starting point of the merged list.
# 2. Maintain a pointer 'current' to build the new list.
# 3. Compare nodes from list1 and list2:
#    - Attach the smaller node to current.next
#    - Move the pointer of that list forward.
# 4. Move 'current' forward.
# 5. When one list ends, attach the remaining part of the other list.
# 6. Return dummy.next as the head of the merged list.

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next

        # Attach remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
