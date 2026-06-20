# LeetCode 135: Candy | Two Pass Greedy

# Approach:
# We assign candies while satisfying both neighbor conditions using two traversals.

# 1. Initialize:
#    - Give each child 1 candy initially.
#    - Create an array 'candies' of size n filled with 1.

# 2. Left to Right pass:
#    - If a child's rating is greater than the previous child's rating,
#      assign one more candy than the previous child.

# 3. Right to Left pass:
#    - If a child's rating is greater than the next child's rating,
#      ensure it has at least one more candy than the next child.
#    - Use max() to preserve candies assigned in the first pass.

# 4. Compute answer:
#    - Sum all values in the candies array.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)

class Solution(object):
    def candy(self, ratings):
        n = len(ratings)

        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
