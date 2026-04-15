# LeetCode 2515: Shortest Distance to Target String in a Circular Array

# Approach:
# We iterate through the array and check all indices where the word matches the target.
# For each such index, we calculate:
# 1. Direct distance = abs(i - startIndex)
# 2. Circular distance = n - abs(i - startIndex)
# We take the minimum of these two distances.
# Finally, we return the smallest distance among all valid indices.
# If target is not found, return -1.

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        min_distance = float('inf')

        for i in range(n):
            if words[i] == target:
                direct = abs(i - startIndex)
                circular = n - direct
                min_distance = min(min_distance, min(direct, circular))

        return min_distance if min_distance != float('inf') else -1
