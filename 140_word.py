# LeetCode 140: Word Break II | DFS + Memoization

# Approach:
# We recursively try every possible prefix starting from the current index.
# Whenever a prefix exists in the dictionary, we recursively solve the
# remaining suffix and combine the results.

# 1. Convert wordDict into a set:
#    - Allows O(1) word lookup.

# 2. Memoization:
#    - Store all possible sentences starting from each index.
#    - Avoids recomputing overlapping subproblems.

# 3. DFS Traversal:
#    - At index i, try every substring s[i:j].
#    - If the substring is a valid word:
#         a) Recursively find all sentences from j onward.
#         b) Append current word to each returned sentence.
#
#    - If j reaches the end of the string, return [""] as the base case.

# 4. Return all constructed sentences.

# 5. Complexity:
#    - Time Complexity: O(N × 2^N) in the worst case
#    - Space Complexity: O(N × 2^N)
#
# where:
# N = length of string s

class Solution(object):
    def wordBreak(self, s, wordDict):

        wordSet = set(wordDict)
        memo = {}

        def dfs(start):

            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            res = []

            for end in range(start + 1, len(s) + 1):

                word = s[start:end]

                if word in wordSet:

                    suffixes = dfs(end)

                    for suffix in suffixes:

                        if suffix:
                            res.append(word + " " + suffix)
                        else:
                            res.append(word)

            memo[start] = res
            return res

        return dfs(0)
