# LeetCode 217 - Contains Duplicate
# Approach: HashSet to track seen elements
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
