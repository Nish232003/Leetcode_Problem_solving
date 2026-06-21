# LeetCode 127: Word Ladder | BFS

# Approach:
# Since each transformation changes only one letter and we need the shortest
# sequence, BFS is ideal because it explores level by level.

# 1. Edge case:
#    - If endWord is not present in wordList, return 0.

# 2. Initialize:
#    - Convert wordList into a set for O(1) lookups.
#    - Use a queue to perform BFS.
#    - Store each word along with its current sequence length.

# 3. BFS Traversal:
#    - Pop a word from the queue.
#    - If it matches endWord, return its level.
#    - Generate all possible one-letter transformations.
#    - If a transformed word exists in the set, push it into the queue
#      with length + 1 and remove it from the set to avoid revisiting.

# 4. If endWord is never reached, return 0.

# 5. Complexity:
#    - Time Complexity: O(N × L × 26)
#    - Space Complexity: O(N)
#
# where:
# N = number of words
# L = length of each word

from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:

            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):

                for ch in "abcdefghijklmnopqrstuvwxyz":

                    new_word = word[:i] + ch + word[i + 1:]

                    if new_word in wordSet:
                        queue.append((new_word, steps + 1))
                        wordSet.remove(new_word)

        return 0
