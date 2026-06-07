# LeetCode 146: LRU Cache | Hash Map + Doubly Linked List

# Approach:
# To achieve O(1) for both get() and put(),
# we use:
#
# 1. Hash Map (Dictionary):
#    - Maps key -> node
#    - Allows O(1) access to any cache entry.
#
# 2. Doubly Linked List:
#    - Maintains usage order.
#    - Most Recently Used (MRU) node is placed near the right.
#    - Least Recently Used (LRU) node is placed near the left.
#
# We use two dummy nodes:
#    left  -> LRU side
#    right -> MRU side
#
# Operations:
#
# Remove Node:
#    - Disconnect node from its neighbors.
#
# Insert Node:
#    - Insert node just before right dummy.
#    - Makes it the most recently used node.
#
# get(key):
#    - If key not present, return -1.
#    - Move node to MRU position.
#    - Return value.
#
# put(key, value):
#    - If key already exists:
#         remove old node.
#    - Insert updated node at MRU position.
#    - If capacity exceeded:
#         remove node next to left dummy
#         (least recently used node).
#
# Complexity:
#    - Time Complexity: O(1)
#    - Space Complexity: O(capacity)


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):

        self.cap = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):

        prev_node = self.right.prev
        next_node = self.right

        prev_node.next = node
        node.prev = prev_node

        node.next = next_node
        next_node.prev = node

    def get(self, key):

        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key, value):

        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)

        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:

            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]
