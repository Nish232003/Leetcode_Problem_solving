# LeetCode 151: Reverse Words in a String | Split and Reverse

# Approach:
# We need to reverse the order of words while removing extra spaces.

# 1. Split the string:
#    - split() automatically removes leading/trailing spaces.
#    - It also handles multiple spaces between words.

# 2. Reverse the list of words.

# 3. Join the words using a single space.

# 4. Return the resulting string.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()

        words.reverse()

        return " ".join(words)
