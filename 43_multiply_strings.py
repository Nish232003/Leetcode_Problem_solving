# LeetCode 43: Multiply Strings | Grade School Multiplication

# Approach:
# 1. Create an array to store multiplication results.
# 2. Multiply every digit of num1 with every digit of num2
#    from right to left.
# 3. Store carry and current digit at proper positions.
# 4. Convert the result array into a string.
# 5. Remove leading zeros.
#
# 6. Complexity:
#    - Time Complexity: O(m * n)
#    - Space Complexity: O(m + n)


class Solution:
    def multiply(self, num1, num2):

        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

                total = mul + res[i + j + 1]

                res[i + j + 1] = total % 10
                res[i + j] += total // 10

        result = ''.join(map(str, res)).lstrip('0')

        return result
