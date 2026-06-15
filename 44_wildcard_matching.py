# LeetCode 44: Wildcard Matching | Greedy + Backtracking

# Approach:
# We use two pointers to traverse the string and pattern.
#
# Wildcards:
#    '?' -> Matches exactly one character.
#    '*' -> Matches any sequence of characters (including empty).
#
# 1. Initialize:
#    - i for string traversal.
#    - j for pattern traversal.
#    - star stores the most recent '*' position.
#    - match stores the string position corresponding to that '*'.
#
# 2. Traverse the string:
#
#    Case 1: Characters match OR pattern has '?'
#         • Move both pointers.
#
#    Case 2: Pattern has '*'
#         • Store star position.
#         • Store current string index in match.
#         • Move pattern pointer.
#
#    Case 3: Mismatch but previous '*' exists
#         • Backtrack to the last '*'.
#         • Let '*' absorb one more character.
#         • Update match and string pointer.
#
#    Case 4: Mismatch and no '*'
#         • Return False.
#
# 3. After string is processed:
#    - Remaining pattern characters must all be '*'.
#
# 4. Complexity:
#    - Time Complexity: O(n + m)
#    - Space Complexity: O(1)


class Solution(object):
    def isMatch(self, s, p):

        i = 0
        j = 0

        star = -1
        match = 0

        while i < len(s):

            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            elif star != -1:
                j = star + 1
                match += 1
                i = match

            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
