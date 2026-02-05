#Leetcode 242 - valid anagram
#Approach : 
#1. Check if both strings have equal length; if not, they cannot be anagrams.
#2. Use a dictionary (hashmap) to store frequency of each character from string s.
#3. Traverse string t and decrease the frequency for each character.
#4. If any character is missing in the dictionary or count becomes incorrect, return False.
#5. Finally, check all values in the dictionary:
#  - if all are 0 → strings are anagrams
#   - otherwise → not anagrams

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count = {}

        for ch in s:
            count[ch] = count.get(ch , 0)+1
        
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1

        for value in count.values():
            if value != 0:
                return False
        return True
