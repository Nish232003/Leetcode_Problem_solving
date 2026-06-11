# LeetCode 188: Best Time to Buy and Sell Stock IV | Dynamic Programming

# Approach:
# We maintain two arrays:
#    - buy[t]  = maximum profit after buying the stock for the t-th transaction.
#    - sell[t] = maximum profit after selling the stock for the t-th transaction.
#
# 1. Handle edge cases:
#    - If k == 0 or prices is empty, return 0.
#
# 2. Optimization:
#    - If k >= len(prices) // 2, transactions are effectively unlimited.
#    - In that case, add all positive price differences.
#
# 3. Initialize:
#    - buy array with negative infinity.
#    - sell array with 0.
#
# 4. Process each price:
#    - Update buy[t]:
#         buy[t] = max(buy[t], sell[t-1] - price)
#
#    - Update sell[t]:
#         sell[t] = max(sell[t], buy[t] + price)
#
# 5. Return:
#    - sell[k] contains the maximum profit after at most k transactions.
#
# Complexity:
#    - Time Complexity: O(n * k)
#    - Space Complexity: O(k)


class Solution(object):
    def maxProfit(self, k, prices):

        n = len(prices)

        if k == 0 or n == 0:
            return 0

        if k >= n // 2:
            profit = 0

            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]

            return profit

        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:

            for t in range(1, k + 1):
                buy[t] = max(buy[t], sell[t - 1] - price)
                sell[t] = max(sell[t], buy[t] + price)

        return sell[k]
