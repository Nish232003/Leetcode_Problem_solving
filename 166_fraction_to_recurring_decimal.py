# LeetCode 166: Fraction to Recurring Decimal | Long Division + Hash Map

# Approach:
# We simulate the long division process.
#
# 1. Handle sign:
#    - If numerator and denominator have opposite signs,
#      prepend '-' to the answer.
#
# 2. Work with absolute values to simplify calculations.
#
# 3. Compute integer part:
#    - numerator // denominator
#    - Append it to the result.
#
# 4. Find remainder:
#    - If remainder == 0, there is no fractional part.
#      Return the result immediately.
#
# 5. Process decimal part:
#    - Append '.' to the answer.
#    - Use a hashmap to store:
#         remainder -> position in result string
#
# 6. Simulate long division:
#    - Multiply remainder by 10.
#    - Append quotient digit.
#    - Update remainder.
#
# 7. Detect repeating cycle:
#    - If a remainder appears again,
#      the decimal starts repeating from its first occurrence.
#    - Insert '(' at the stored position
#      and ')' at the end.
#
# 8. Complexity:
#    - Time Complexity: O(k)
#      (k = number of digits generated)
#    - Space Complexity: O(k)


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):

        if numerator == 0:
            return "0"

        result = []

        if (numerator < 0) ^ (denominator < 0):
            result.append('-')

        numerator = abs(numerator)
        denominator = abs(denominator)

        result.append(str(numerator // denominator))

        remainder = numerator % denominator

        if remainder == 0:
            return "".join(result)

        result.append('.')

        seen = {}

        while remainder:

            if remainder in seen:
                idx = seen[remainder]
                result.insert(idx, '(')
                result.append(')')
                break

            seen[remainder] = len(result)

            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)
