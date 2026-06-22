# LeetCode 1833: Maximum Ice Cream Bars | Counting Sort + Greedy

# Approach:
# Instead of sorting the entire array, we use counting sort to count the
# frequency of each cost and buy the cheapest ice cream bars first.

# 1. Count frequencies:
#    - Create a frequency array where freq[i] stores the number of bars
#      having cost i.

# 2. Traverse costs in increasing order:
#    - Start from the cheapest cost.
#    - Determine how many bars of that cost can be bought with remaining coins.

# 3. Update answer:
#    - Add the number of bars purchased to the answer.
#    - Deduct the corresponding amount from coins.

# 4. Continue until:
#    - Coins become insufficient, or
#    - All costs have been processed.

# 5. Complexity:
#    - Time Complexity: O(n + m)
#      where m = max(costs)
#    - Space Complexity: O(m)


class Solution(object):
    def maxIceCream(self, costs, coins):

        freq = [0] * (max(costs) + 1)

        for cost in costs:
            freq[cost] += 1

        ans = 0

        for cost in range(1, len(freq)):

            if coins < cost:
                break

            can_buy = min(freq[cost], coins // cost)

            ans += can_buy
            coins -= can_buy * cost

        return ans
