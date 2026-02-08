#Leetcode : 26 Remove Duplicates from sorted Array
#Leetcode link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

#Approach :
# We will use two pointers approach to solve this problem.
#First we will check our array wheather it is empty if it is we will return 0
# Since we have sorted array so duplicates will be adjacent to each other.
# 1st pointer will track last unique elements
# 2nd pointer will traverse.

#Time complexity : O(n)
#Space complexity : O(1)

class Solution(object):
  def removeDuplicates( self , nums):
    if len(nums) == 0:
      return 0
    i = 0
    for j in range( 1 , len(nums)):
      if nums[j] != nums[i]
      i += 1
      nums[i] = nums[j]
    return i+1
