#Leetcode : 121 Best Time to buy and sell stock

#Approach:
# We use two pointers l (buy day) and r (sell day)
# l represents the minimum price seen so far  r iterates through the array

# If prices[r] > prices[l], we calculate profit and update maximum profit

# If prices[r] < prices[l], we update l = r because we found a better buying day

# We move r forward in every step
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxProfit(self, prices):
        l ,r = 0,1
        maxP = 0
        while r<len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP , profit)
            else:
                l = r
            r += 1
        return maxP
