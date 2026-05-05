# Merge K Sorted Linked Lists using Min Heap (Priority Queue)

#Approach:
#1. Push first node of each list into min heap
#2. Extract smallest node and attach to result list
#3. Push next node of extracted element into heap
#4. Repeat until heap is empty

import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        
        
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        current = dummy
        
        
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
