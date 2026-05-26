# LeetCode: 3120 Count the Number of Special Characters I

# Approach:
# We use two sets to track:
#   • lowercase letters
#   • uppercase letters (converted to lowercase)
#
# 1. Traverse the string:
#    - If character is lowercase, store it in 'lower'.
#    - If character is uppercase, convert it to lowercase
#      and store it in 'upper'.
#
# 2. Find common characters:
#    - The intersection of both sets gives letters
#      present in both lowercase and uppercase forms.
#
# 3. Return the count of common letters.
#
# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def numberOfSpecialChars(self, word):

        lower = set()
        upper = set()

        
        for ch in word:

            if 'a' <= ch <= 'z':
                lower.add(ch)

            else:
                upper.add(ch.lower())

        
        return len(lower & upper)
