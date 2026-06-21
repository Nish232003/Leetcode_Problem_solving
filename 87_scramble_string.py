# LeetCode 87: Scramble String | Recursion + Memoization + Pruning

# Approach:
# Instead of generating all possible scrambled strings, we recursively check
# whether two substrings can be transformed into each other.

# 1. Base cases:
#    - If both strings are identical, return True.
#    - If their sorted characters differ, return False since they cannot
#      be scrambled versions of each other.

# 2. Memoization:
#    - Store results of previously computed (s1, s2) pairs to avoid
#      redundant recursive calculations.

# 3. Try every possible split position:
#    - For each index i from 1 to n-1, consider two cases:
#
#      a) No Swap:
#         s1[:i]  ↔ s2[:i]
#         s1[i:]  ↔ s2[i:]
#
#      b) Swap:
#         s1[:i]  ↔ s2[n-i:]
#         s1[i:]  ↔ s2[:n-i]
#
#    - If both parts match recursively in either case, return True.

# 4. Store result in memo and return.

# 5. Complexity:
#    - Time Complexity: O(n^4)
#    - Space Complexity: O(n^3)


class Solution(object):
    def isScramble(self, s1, s2):

        memo = {}

        def dfs(a, b):

            if a == b:
                return True

            if sorted(a) != sorted(b):
                return False

            if (a, b) in memo:
                return memo[(a, b)]

            n = len(a)

            for i in range(1, n):

                # Case 1: Without swapping
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True

                # Case 2: With swapping
                if dfs(a[:i], b[n - i:]) and dfs(a[i:], b[:n - i]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return dfs(s1, s2)
