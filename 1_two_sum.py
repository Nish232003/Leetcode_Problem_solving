#Leetcode : 1 Two Sum
#Leetcode link : https://leetcode.com/problems/two-sum/

#Approach : 
#The goal is to find two indices in the array such that their values add up to the given target. Instead of checking every possible pair , we use a hash map to store elements we have already seen while traversing the array.
#Time complexity : O(n)
#Space complexity : O(n)
#Steps :
# 1.Traverse the array only once.
# 2.For every element, calculate what value is needed to reach the target: complement = target − current element
# 3.Before moving ahead, check if this complement already exists in a hash map.
# 4.If it exists → we already saw the number that forms the required sum, so return both indices.
# 5.If it doesn’t exist → store the current element and its index in the hash map.
# 6.Continue this process until the pair is found.

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i , num in enumerate(nums):
            remaining = target - num

            if remaining in seen:
                return [seen[remaining] , i]
            
            seen[num] = i
       
