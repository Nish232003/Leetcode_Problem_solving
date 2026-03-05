# Leetcode : 160 Intersection of Two Linked Lists
# Leetcode link : https://leetcode.com/problems/intersection-of-two-linked-lists/

# Approach :
# We use the Two Pointer technique.
# Two pointers traverse both linked lists.

# Time Complexity : O(n + m)
# Space Complexity : O(1)

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        pA = headA
        pB = headB
        
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA
