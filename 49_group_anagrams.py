#Leetcode : 49 Group Anagram
#Approach :
#Since anagrams are just rearrangements of the same characters, sorting them gives an identical key. 
#I'll use a hashmap — sorted tuple as key, list of anagrams as value. Iterate through all words, sort each one, append to its group, and return the values at the end

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        mp = defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            mp[key].append(word)
        
        return list(mp.values())
