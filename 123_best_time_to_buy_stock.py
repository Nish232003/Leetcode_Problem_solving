# LeetCode 123: Best Time to Buy and Sell Stock III | State Machine DP

# Approach:
# We are allowed to make at most two transactions.
#
# Instead of using a DP table, we track four states:
#
# 1. first_buy
#    - Maximum profit after buying the first stock.
#
# 2. first_sell
#    - Maximum profit after selling the first stock.
#
# 3. second_buy
#    - Maximum profit after buying the second stock.
#
# 4. second_sell
#    - Maximum profit after selling the second stock.
#
# For each price:
#
# first_buy  = max(first_buy, -price)
# first_sell = max(first_sell, first_buy + price)
#
# second_buy = max(second_buy, first_sell - price)
# second_sell= max(second_sell, second_buy + price)
#
# The answer is stored in second_sell.
#
# Example:
# prices = [3,3,5,0,0,3,1,4]
#
# First transaction:
# Buy at 0, Sell at 3 → Profit = 3
#
# Second transaction:
# Buy at 1, Sell at 4 → Profit = 3
#
# Total Profit = 6
#
# Complexity:
# - Time Complexity: O(n)
# - Space Complexity: O(1)


class Solution(object):
    def maxProfit(self, prices):

        first_buy = float('-inf')
        first_sell = 0

        second_buy = float('-inf')
        second_sell = 0

        for price in prices:

            first_buy = max(first_buy, -price)

            first_sell = max(first_sell,
                             first_buy + price)

            second_buy = max(second_buy,
                             first_sell - price)

            second_sell = max(second_sell,
                              second_buy + price)

        return second_sell
