# LeetCode 38: Count and Say | Run-Length Encoding Simulation

# Approach:
# Instead of generating the sequence directly, we repeatedly build the next term
# by counting consecutive identical digits in the current term.
#
# 1. Start with the base string:
#    - countAndSay(1) = "1"
#
# 2. For each iteration:
#    - Traverse the current string.
#    - Count consecutive occurrences of the same digit.
#    - Append:
#        • Frequency of the digit
#        • The digit itself
#
# 3. Build the next sequence string:
#    - Continue until all groups are processed.
#
# 4. Repeat this process (n - 1) times.
#
# 5. Complexity:
#    - Time Complexity: O(m), where m is the length of the generated string.
#    - Space Complexity: O(m)


class Solution:
    def countAndSay(self, n: int) -> str:

        s = "1"

        for _ in range(n - 1):

            result = []
            i = 0

            while i < len(s):

                count = 1

                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1

                result.append(str(count))
                result.append(s[i])

                i += 1

            s = "".join(result)

        return s
