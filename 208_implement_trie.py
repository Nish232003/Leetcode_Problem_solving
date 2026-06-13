# LeetCode 208: Implement Trie (Prefix Tree)

# Approach:
# A Trie stores characters as nodes in a tree-like structure.
# Each node keeps:
#    - children: mapping of character -> next node
#    - end: marks whether a word ends at this node

# 1. Insert:
#    - Traverse each character of the word.
#    - Create a new node if the character does not exist.
#    - Move to the next node.
#    - Mark the last node as end of a word.

# 2. Search:
#    - Traverse the trie character by character.
#    - If any character is missing, return False.
#    - After traversal, return True only if the current node
#      marks the end of a word.

# 3. startsWith:
#    - Traverse the trie using the prefix.
#    - If any character is missing, return False.
#    - If traversal succeeds, return True.

# 4. Complexity:
#    - Insert: O(n)
#    - Search: O(n)
#    - startsWith: O(n)
#    - Space Complexity: O(total characters inserted)


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.end = True

    def search(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return node.end

    def startsWith(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return True
