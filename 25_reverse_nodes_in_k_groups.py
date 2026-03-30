# LeetCode 25: Reverse Nodes in k-Group

# Approach:
# We reverse the linked list in groups of size k.
# First, we check if k nodes are available.
# If yes, we reverse that group and connect it back.
# If not, we leave remaining nodes as it is.
# A dummy node is used to simplify pointer handling.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        while True:
            kth = self.findKth(prev_group, k)
            if not kth:
                break
            
            next_group = kth.next
            
            prev = next_group
            curr = prev_group.next
            
            
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp
        
        return dummy.next

    def findKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
