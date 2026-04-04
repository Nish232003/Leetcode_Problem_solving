#Leetcode : 125 Valid Palindrome
#Approach
#1. Initialize an empty list to store valid characters.
#2. Traverse the input string and filter only alphanumeric characters.
#3. Convert each valid character to lowercase and append to the list.
#4. Join the list into a cleaned string.
#5. Compare the cleaned string with its reverse.
#6. If both are equal, return True (palindrome), else return False.

class Solution(object):
    def isPalindrome(self, s):
        cleaned = []
        
        for ch in s:
            if ch.isalnum():
                cleaned.append(ch.lower())
        
        cleaned = "".join(cleaned)
        
        return cleaned == cleaned[::-1]
