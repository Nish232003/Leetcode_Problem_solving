# LeetCode 3121: Count the Number of Special Characters II | HashMap + Index Tracking

# Approach:
# Instead of checking every character repeatedly, we track:
# - The last occurrence of every lowercase letter
# - The first occurrence of every uppercase letter
#
# A character is special if:
# 1. It appears in both lowercase and uppercase
# 2. All lowercase occurrences appear before the first uppercase occurrence

# 1. Initialize:
#    - 'last_lower'  -> stores last index of lowercase letters
#    - 'first_upper' -> stores first index of uppercase letters

# 2. Traverse the string:
#    - If character is lowercase:
#         update its latest index
#    - If character is uppercase:
#         store only its first occurrence

# 3. Check valid special characters:
#    - For every lowercase character:
#         • Convert it to uppercase
#         • Ensure uppercase exists
#         • Ensure last lowercase index < first uppercase index

# 4. Count all valid characters

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """

        first_upper = {}
        last_lower = {}

        
        for i, ch in enumerate(word):

            if ch.islower():
                last_lower[ch] = i

            else:
                if ch not in first_upper:
                    first_upper[ch] = i

        
        count = 0

        for ch in last_lower:

            up = ch.upper()

            if up in first_upper and last_lower[ch] < first_upper[up]:
                count += 1

        
        return count
