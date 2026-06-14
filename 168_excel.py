# LeetCode 168: Excel Sheet Column Title | Base-26 Conversion

# Approach:
# Excel columns follow a modified Base-26 system:
#
# A -> 1
# B -> 2
# ...
# Z -> 26
# AA -> 27
#
# Unlike normal Base-26, there is no digit '0'.
# Therefore, before taking modulo, we subtract 1.
#
# 1. While columnNumber > 0:
#    - Subtract 1 from columnNumber.
#    - Find current character:
#         chr(columnNumber % 26 + ord('A'))
#    - Append it to the answer.
#    - Divide columnNumber by 26.
#
# 2. Characters are generated from right to left,
#    so reverse the result at the end.
#
# 3. Complexity:
#    - Time Complexity: O(log26 n)
#    - Space Complexity: O(log26 n)


class Solution(object):
    def convertToTitle(self, columnNumber):

        result = []

        while columnNumber:

            columnNumber -= 1

            result.append(
                chr(columnNumber % 26 + ord('A'))
            )

            columnNumber //= 26

        return "".join(result[::-1])
