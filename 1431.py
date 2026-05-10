#Leetcode 1431
#Approach 
#First we will find max(Candies) then we will run a loop in which we will be adding extra candies to each number and then using comparison operator we will compare it with max(Candies)
#If it is greater then we will return True otherwise we will returN False

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        ans = []
        for i in candies:
            if (i+extraCandies) >= max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans
