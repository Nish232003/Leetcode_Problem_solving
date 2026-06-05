# LeetCode 138: Copy List with Random Pointer | Hash Map

# Approach:
# We create a mapping between each original node and its cloned node.

# 1. Handle edge case:
#    - If the list is empty, return None.

# 2. First Pass:
#    - Traverse the original list.
#    - Create a clone for every node.
#    - Store mapping:
#         original_node -> cloned_node

# 3. Second Pass:
#    - Traverse the original list again.
#    - Set:
#         clone.next = clone of original.next
#         clone.random = clone of original.random

# 4. Return:
#    - Return the clone corresponding to the original head.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


class Solution(object):
    def copyRandomList(self, head):

        if not head:
            return None

        mp = {}

        curr = head
        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            mp[curr].next = mp.get(curr.next)
            mp[curr].random = mp.get(curr.random)
            curr = curr.next

        return mp[head]
