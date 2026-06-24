# LeetCode 3612: Process String with Special Operations I | String Simulation

# Approach:
# Simulate the operations from left to right.
#
# 1. Initialize an empty string result.
#
# 2. Traverse each character:
#    - Letter  -> append to result.
#    - '*'     -> remove last character if present.
#    - '#'     -> duplicate current result.
#    - '%'     -> reverse current result.
#
# 3. Return the final result.
#
# 4. Complexity:
#    - Time Complexity: O(n * m)
#      (string duplication/reversal may process current string)
#    - Space Complexity: O(m)
#      where m is the final string length.


class Solution:
    def processStr(self, s: str) -> str:
        res = ""

        for ch in s:
            if 'a' <= ch <= 'z':
                res += ch
            elif ch == '*':
                res = res[:-1]
            elif ch == '#':
                res += res
            else:
                res = res[::-1]

        return res
