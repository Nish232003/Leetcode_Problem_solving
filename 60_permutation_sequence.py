# LeetCode 60: Permutation Sequence | Math + Factorial Logic

# Approach:
# Instead of generating all permutations, we directly build
# the k-th permutation using factorials.

# Key Idea:
# For n numbers:
#    - Total permutations = n!
#    - Each starting digit repeats for (n-1)! permutations.
#
# We use this to determine which digit should come at each position.

# 1. Initialize:
#    - Create list of numbers from 1 to n.
#    - Precompute factorial values.
#    - Convert k to 0-based indexing (k -= 1).

# 2. Build permutation:
#    - Find index using:
#         index = k // factorial(remaining_digits)
#    - Append selected number to answer.
#    - Remove used number from list.
#    - Update k:
#         k %= factorial(remaining_digits)

# 3. Repeat until all digits are used.

# 4. Complexity:
#    - Time Complexity: O(n^2)
#    - Space Complexity: O(n)


class Solution(object):
    def getPermutation(self, n, k):

        
        numbers = [str(i) for i in range(1, n + 1)]

        
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i

        
        k -= 1

        result = ""

        
        for i in range(n, 0, -1):

            
            index = k // factorial[i - 1]

            
            result += numbers[index]

            
            numbers.pop(index)

            
            k %= factorial[i - 1]

        
        return result
