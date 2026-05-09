#Leetcode : 1523 
#Approach :

#Count total odd numbers from 1 to high
#Count total odd numbers before low
#Subtract both counts to get odd numbers in the required range

class Solution(object):
    def countOdds(self, low, high):
       return (high+1)//2 - (low//2)
