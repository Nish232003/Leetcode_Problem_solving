# LeetCode 61: Rotate List

### Tags

#LinkedList #TwoPointers #InterviewPrep #O(n) #InPlace

### Approach

#* Calculate the length of the linked list
#* Convert the list into a circular linked list
#* Optimize rotations using k % n
#* Find the new tail at position (n - k - 1)
#* Break the cycle to get the rotated list

### Complexity

#* Time Complexity: O(n)
#* Space Complexity: O(1)

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        tail = head
        
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        tail.next = head
        
        steps_to_new_tail = length - k - 1
        new_tail = head
        
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
```
