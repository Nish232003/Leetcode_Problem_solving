#Approach : Add efficient prefix-sum + hashmap solution for Subarray Sum Equals K

#* Implemented optimal O(n) solution using running prefix sum and frequency map
#* Counts subarrays where (current_sum − k) has appeared before
#* Handles negative numbers and overlapping subarrays correctly
#* Added initial hashmap entry {0:1} to support subarrays starting from index 0

#Time Complexity: O(n)
#Space Complexity: O(n)

class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        freq = {0: 1}  
        
        for num in nums:
            prefix_sum += num
            
          
            if (prefix_sum - k) in freq:
                count += freq[prefix_sum - k]
            
          
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
        
        return count
