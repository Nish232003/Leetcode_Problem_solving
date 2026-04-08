#Leetcode : 128 longest consecutive sequence
#Approach : We use a HashSet to achieve O(n) time complexity.
#First, we insert all elements into a set for constant-time lookup.
#Then, we iterate through the set and only start building a sequence when the current number is the beginning of a sequence, i.e., when (num - 1) is not present in the set.
#From there, we keep checking for consecutive numbers (num + 1, num + 2, …) and count the length of the sequence.
#We update the maximum length accordingly.

class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:  
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
