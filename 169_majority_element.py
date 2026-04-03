#Leetcode : 169 Majority Element
#Approach :
#We use a hashmap (count dictionary) to store the frequency of each element.
#While traversing the array, we increment the count of each element.
#If at any point, the frequency of an element becomes greater than n/2,
#we return that element as the majority element.

class Solution(object):
  def majorityElement(self , nums):
    count = {}
    for num in nums:
      if num in count:
        count[num] += 1
      else:
        count[num] = 1
      if count[num] > len(nums)//2:
        return num
