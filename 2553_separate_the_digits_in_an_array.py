#Leetcode : 2553

#Approach
#Traverse each number in nums.
#Convert the number into a string so each digit can be accessed easily.
#Convert every character back to integer using map(int, str(n)).
#Add all digits into the answer list while maintaining order.

class Solution(object):
    def separateDigits(self, nums):
      
        ans = []
        
        for n in nums:
            ans.extend(map(int, str(n)))
            
        return ans
