# LeetCode 796: Rotate String

# Approach:
# If s can be rotated to become goal,
# then goal must be a substring of s + s

class Solution(object):
    def rotateString(self, s, goal):
        
        if len(s) != len(goal):
            return False

        return goal in (s + s)
