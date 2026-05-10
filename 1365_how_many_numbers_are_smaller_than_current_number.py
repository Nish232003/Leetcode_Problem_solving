#Leetcode : 1365 :   How many numbers are smaller than current number?
#Approach :
#We create a result list ans to store the count of numbers smaller than each nums[i]. For every element in the array, we traverse the entire array again and compare it with all other elements using the < operator. If an element is smaller than the current number, we increment the counter. After completing all comparisons for one element, we append the final count to the answer list. Finally, we return the result list.

class solution(object):
  class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans = []
        for i in nums:
          c = 0
          for j in nums:
            if j<1:
              c +=1
          ans.append(c)
       return ans      
