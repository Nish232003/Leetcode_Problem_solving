# Leetcode : 58 Length of Last Word
# Leetcode link : https://leetcode.com/problems/length-of-last-word/

# Approach :
# The goal is to find the length of the last word in the given string.
# A word is defined as a sequence of non-space characters.
# We traverse the string from the end and count characters until a space is found.

# Time complexity : O(n)
# Space complexity : O(1)

# Steps :
# 1. Remove trailing spaces from the string.
# 2. Start traversing from the end of the string.
# 3. Count characters until a space is encountered.
# 4. Return the count as the length of the last word.

class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        length = 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                break
            length += 1
        
        return length
