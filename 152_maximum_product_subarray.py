#Leetcode : 152 Maximum product subarray
#Approach
#We iterate through the array while maintaining both current maximum and minimum products, since a negative number can flip signs. At each step, we choose the best among starting fresh or extending previous products, and update the global maximum

class Solution(object):
    def maxProduct(self, nums):
        current_max = nums[0]
        current_min = nums[0]
        max_product = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            
            temp = current_max
            
            current_max = max(num, current_max * num, current_min * num)
            current_min = min(num, temp * num, current_min * num)
            
            max_product = max(max_product, current_max)
        
        return max_product
