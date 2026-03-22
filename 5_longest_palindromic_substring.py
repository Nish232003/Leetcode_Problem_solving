# LeetCode 5: Longest Palindromic Substring | Two Pointers + Expand Around Center

# Approach:
# Instead of checking all substrings (O(n^3)), we optimize using center expansion.

# 1. A palindrome mirrors around its center.
#    So for each index, we try to expand around it.

# 2. Handle two cases:
#    - Odd length palindrome (center at i)
#    - Even length palindrome (center between i and i+1)

# 3. For each center:
#    - Expand left and right pointers while characters match.
#    - Extract the valid palindrome substring.

# 4. Keep track of the longest palindrome found.

# 5. Return the longest substring.

class Solution(object):
    def longestPalindrome(self, s):

        # Helper function to expand around center
        def expand(left, right):
            # Expand while valid palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring
            return s[left+1:right]

        result = ""

        for i in range(len(s)):

            # Case 1: Odd length palindrome
            odd = expand(i, i)

            # Case 2: Even length palindrome
            even = expand(i, i + 1)

            # Update result with the longer palindrome
            if len(odd) > len(result):
                result = odd

            if len(even) > len(result):
                result = even

        return result
