# Leetcode : 20 Valid Parentheses
# Leetcode link : https://leetcode.com/problems/valid-parentheses/

# Approach :
# We use a stack to keep track of opening brackets.
# Traverse the string character by character.

# Time Complexity : O(n)
# Space Complexity : O(n)


class Solution(object):
    def isValid(self, s):

        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:

            if char in mapping:

                top = stack.pop() if stack else '#'

                if mapping[char] != top:
                    return False

            else:
                stack.append(char)

        return not stack
