# LeetCode 126: Word Ladder II | BFS + Backtracking

# Approach:
# We first use BFS to find the shortest distance from beginWord to every
# reachable word while simultaneously storing parent relationships.
# Then, we use DFS backtracking to reconstruct all shortest paths.

# 1. Edge case:
#    - If endWord is not present in wordList, return [].

# 2. BFS Traversal:
#    - Start from beginWord.
#    - Generate all possible one-letter transformations.
#    - Store each word's parents to reconstruct paths later.
#    - Maintain levels to ensure only shortest paths are considered.
#    - Stop BFS after reaching endWord's level.

# 3. Backtracking:
#    - Starting from endWord, recursively move through its parents.
#    - Build paths in reverse order.
#    - Reverse each completed path before adding to the answer.

# 4. Return all shortest transformation sequences.

# 5. Complexity:
#    - Time Complexity: O(N × L × 26)
#    - Space Complexity: O(N × L)
#
# where:
# N = number of words
# L = length of each word

from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = {beginWord: 0}

        queue = deque([beginWord])

        while queue:

            size = len(queue)
            found = False

            for _ in range(size):

                word = queue.popleft()

                for i in range(len(word)):

                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        new_word = word[:i] + ch + word[i + 1:]

                        if new_word not in wordSet:
                            continue

                        if new_word not in level:
                            level[new_word] = level[word] + 1
                            queue.append(new_word)

                        if level[new_word] == level[word] + 1:
                            parents[new_word].append(word)

                        if new_word == endWord:
                            found = True

            if found:
                break

        ans = []

        def dfs(word, path):

            if word == beginWord:
                ans.append(path[::-1])
                return

            for parent in parents[word]:
                dfs(parent, path + [parent])

        dfs(endWord, [endWord])

        return ans
