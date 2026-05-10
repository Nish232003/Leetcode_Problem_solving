#Leetcode : 09  : Palindrome Number
#Approach : 
#- Store the original number in a temporary variable.
#- Reverse the number by extracting digits one by one using modulo (% 10).
#- Build the reversed number using:
#  rev = rev * 10 + digit
#- Remove the last digit each iteration using integer division (// 10).
#- After reversing, compare the reversed number with the original number.
#- If both are equal, the number is a palindrome; otherwise, it is not.

Time Complexity: O(d)
Space Complexity: O(1)
class Solution(object):
    def isPalindrome(self, x):
        temp = x
        rev = 0
        while temp>0:
            r = temp%10
            temp //= 10
            rev = rev*10 + r
        if rev == x:
            return True
        else:
            return False
        
