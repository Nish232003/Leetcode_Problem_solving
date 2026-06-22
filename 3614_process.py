# LeetCode 3614: Process String with Special Operations II | Reverse Simulation

# Approach:
# Instead of constructing the final string (which may have length up to 10^15),
# we track only the length after each operation and then work backwards to locate
# the kth character.

# 1. Compute lengths:
#    - Letter: increase length by 1.
#    - '*': decrease length by 1 if possible.
#    - '#': double the current length.
#    - '%': length remains unchanged.

# 2. Handle invalid k:
#    - If k is outside the final length, return '.'.

# 3. Traverse operations in reverse:
#    - Undo each operation while updating k.
#    - '#': if k is in the second half, map it to the first half.
#    - '%': reverse index → k = length - 1 - k.
#    - '*': before deletion, length was one larger.
#    - Letter: if k points to this character, return it.

# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


class Solution(object):
    def processStr(self, s, k):

        lengths = [0]

        for ch in s:
            cur = lengths[-1]

            if 'a' <= ch <= 'z':
                cur += 1
            elif ch == '*':
                if cur:
                    cur -= 1
            elif ch == '#':
                cur *= 2

            lengths.append(cur)

        if k >= lengths[-1]:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            cur = lengths[i + 1]
            prev = lengths[i]

            if ch == '#':
                if k >= prev:
                    k -= prev

            elif ch == '%':
                k = cur - 1 - k

            elif ch == '*':
                pass

            else:
                if k == prev:
                    return ch

        return '.'
