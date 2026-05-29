# LeetCode 67: Add Binary | Simulation + Carry Handling

# Approach:
# Instead of converting binary strings to integers,
# we simulate binary addition from right to left.

# 1. Initialize:
#    - Use two pointers:
#        • i for string 'a'
#        • j for string 'b'
#    - Use 'carry' to store overflow.
#    - Use 'result' list to build answer.

# 2. Traverse from end:
#    - Add current digits from both strings.
#    - Add carry from previous step.
#    - Append (total % 2) to result.
#    - Update carry as (total // 2).

# 3. Continue until:
#    - Both strings are processed
#    - AND no carry remains.

# 4. Reverse result:
#    - Since digits are added from right to left.

# 5. Complexity:
#    - Time Complexity: O(max(n, m))
#    - Space Complexity: O(max(n, m))


class Solution(object):
    def addBinary(self, a, b):

        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:

            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return "".join(result[::-1])
