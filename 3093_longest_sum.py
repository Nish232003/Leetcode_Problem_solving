# LeetCode 3093: Longest Common Suffix Queries | Trie + Reversed String Matching

# Approach:
# Instead of checking every query against all container words,
# we use a Trie built on reversed strings to efficiently find
# the longest common suffix.

# 1. Create TrieNode:
#    - Each node stores:
#        • children -> next characters
#        • idx -> index of the best word for that suffix
#
#    - "Best word" means:
#        • Shortest length
#        • If tie, earlier occurrence

# 2. Build Trie using reversed words:
#    - Reverse every word from wordsContainer.
#    - Insert character by character into Trie.
#    - At every node, update the best index.

# 3. Process each query:
#    - Reverse query string.
#    - Traverse Trie as long as characters match.
#    - The deepest reachable node contains the answer index.

# 4. Return all answers.

# 5. Complexity:
#    - Time Complexity: O(total characters in wordsContainer + wordsQuery)
#    - Space Complexity: O(total Trie nodes)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1


class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """

        root = TrieNode()

        
        
        for i, word in enumerate(wordsContainer):

            node = root

            
            
            if (node.idx == -1 or
                len(wordsContainer[i]) < len(wordsContainer[node.idx])):
                node.idx = i

            
            
            for ch in reversed(word):

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                
                
                if (node.idx == -1 or
                    len(wordsContainer[i]) < len(wordsContainer[node.idx])):
                    node.idx = i

        
        ans = []

        
        
        for word in wordsQuery:

            node = root

            
            
            for ch in reversed(word):

                if ch not in node.children:
                    break

                node = node.children[ch]

            ans.append(node.idx)

        
        return ans
