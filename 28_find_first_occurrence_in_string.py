# Add an efficient solution for LeetCode 28: Find the Index of the First Occurrence in a String.
# The approach uses a sliding window to compare substrings of the haystack with the needle.
# Returns the starting index of the first occurrence, or -1 if the needle is not present.

# Time Complexity: O(n * m)
# Space Complexity: O(1)

class Solution(object):
    def strStr(self, haystack, needle):
        

        n, m = len(haystack), len(needle)
      
        if m == 0:
            return 0

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1
