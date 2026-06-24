# LeetCode 2130: Maximum Twin Sum of a Linked List | Fast & Slow Pointers + Reverse List

# Approach:
# To compute twin sums efficiently, reverse the second half of the list.
#
# 1. Find the middle:
#    - Use slow and fast pointers.
#    - When fast reaches the end, slow points to the start
#      of the second half.
#
# 2. Reverse the second half of the linked list.
#
# 3. Traverse both halves together:
#    - First pointer starts from head.
#    - Second pointer starts from reversed second half.
#    - Compute twin sum = first.val + second.val.
#    - Track the maximum twin sum.
#
# 4. Return the maximum value found.
#
# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution:
    def pairSum(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        ans = 0
        first = head
        second = prev

        while second:
            ans = max(ans, first.val + second.val)
            first = first.next
            second = second.next

        return ans
