#Leetcode : 344 Reverse String
#Approach:
#Use two pointers, one starting from the beginning and one from the end of the array. 
#Swap the characters at both pointers and move them towards each other until they meet.
class Solution(object):
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
