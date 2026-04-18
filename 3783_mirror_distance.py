#Leetcode:  '3783. Mirror Distance of an Integer' problem

# Approach:
# We reverse the digits of the given integer and compute the absolute difference.
# Steps:
# 1. Convert the integer to string and reverse it.
# 2. Convert reversed string back to integer.
# 3. Return absolute difference between original and reversed number.

# Time Complexity: O(d)
# Space Complexity: O(1)

class Solution(object):
    def mirrorDistance(self, n):
        rev = int(str(n)[::-1])
        return abs(n - rev)
