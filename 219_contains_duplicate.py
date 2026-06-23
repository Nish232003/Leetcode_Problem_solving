# LeetCode 219: Contains Duplicate II | Hash Map + Last Seen Index

# Approach:
# Instead of comparing every pair of elements, we store the most recent
# index of each number using a hash map.

# 1. Initialize:
#    - Create a dictionary 'last_index' to store the latest index
#      where each number appeared.

# 2. Traverse the array:
#    - For each number, check if it already exists in the dictionary.
#    - If it exists and the difference between the current index and
#      its previous index is <= k, return True.
#    - Update the current index of the number in the dictionary.

# 3. If no such pair is found after traversing the entire array,
#    return False.

# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

        last_index = {}

        for i, num in enumerate(nums):

            if num in last_index and i - last_index[num] <= k:
                return True

            last_index[num] = i

        return False
