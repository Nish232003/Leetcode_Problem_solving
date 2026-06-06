# LeetCode 122: Best Time to Buy and Sell Stock II | Greedy Approach

# Approach:
# Since multiple transactions are allowed, we can profit from every
# upward price movement.
#
# 1. Initialize profit = 0.
#
# 2. Traverse the array from index 1 to n-1:
#    - If today's price is greater than yesterday's price,
#      add the difference to profit.
#
# 3. Return the total profit.
#
# Why it works:
# - Every increasing segment contributes to the maximum profit.
# - Instead of finding local minima and maxima explicitly,
#   we simply capture all positive gains.
#
# Example:
# prices = [7,1,5,3,6,4]
#
# Profit:
# 1 -> 5 = +4
# 3 -> 6 = +3
#
# Total Profit = 7
#
# Complexity:
# - Time Complexity: O(n)
# - Space Complexity: O(1)


class Solution(object):
    def maxProfit(self, prices):

        profit = 0

        for i in range(1, len(prices)):

            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
