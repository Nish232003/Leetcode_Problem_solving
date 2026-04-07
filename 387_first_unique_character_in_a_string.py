#Leetcode : 387 : First unique character in a string
#Approach:
# We will use hashmap to count the frequency of each character then traverse to find the character with count = 1 and return index if not found return -1

from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
       count = Counter(s)
       for i  , ch in enumerate(s):
        if count[ch] == 1:
            return i
       return -1
