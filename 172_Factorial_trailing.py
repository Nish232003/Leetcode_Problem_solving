# LeetCode 172: Factorial Trailing Zeroes | Counting Factors of 5

# Approach:
# A trailing zero is formed by a pair of:
#    • 2 × 5
#
# In a factorial, factors of 2 are much more frequent than factors of 5.
# Therefore, the number of trailing zeroes depends only on
# how many times 5 appears as a factor.

# 1. Initialize:
#    - Create a variable 'count' to store the total number
#      of factors of 5.

# 2. Repeatedly divide n by 5:
#    - n //= 5 gives the count of numbers contributing
#      at least one factor of 5.
#    - Add this value to count.
#
# 3. Continue:
#    - Numbers like 25, 125, 625 contribute extra factors of 5.
#    - Therefore keep dividing by 5 until n becomes 0.

# 4. Return:
#    - count stores the total number of trailing zeroes.

# 5. Complexity:
#    - Time Complexity: O(log₅ n)
#    - Space Complexity: O(1)


class Solution:
    def trailingZeroes(self, n: int) -> int:

        count = 0

        while n:

            n //= 5
            count += n

        return count
