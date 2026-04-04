#Leetcode : 53 Maximum subarray
#Approach :
#We iterate through the array while maintaining a running sum. At each step, we choose whether to extend the current subarray or start a new one. We continuously update the maximum subarray sum encountered.

class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1 , len(nums)):
            current_sum = max(nums[i] , current_sum+nums[i])
            max_sum = max(max_sum , current_sum)

        return max_sum
