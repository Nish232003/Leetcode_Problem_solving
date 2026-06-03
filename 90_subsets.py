# LeetCode 90: Subsets II | Backtracking

# Approach:
# Since the array may contain duplicates, we first sort the array
# so that duplicate elements become adjacent.
#
# 1. Sort nums.
#
# 2. Use backtracking to generate all possible subsets.
#    - At each step, add the current subset to the result.
#    - Try including each remaining element.
#
# 3. Skip duplicates:
#    - If nums[i] is the same as nums[i - 1]
#      and both are at the same recursion level,
#      skip nums[i].
#
# 4. Continue exploring by adding the element,
#    then backtrack to try other possibilities.
#
# Example:
# nums = [1,2,2]
#
# Generated subsets:
# []
# [1]
# [1,2]
# [1,2,2]
# [2]
# [2,2]
#
# Complexity:
# Time Complexity: O(2^n)
# Space Complexity: O(n)   (recursion stack)


class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()

        result = []

        def backtrack(start, subset):
            result.append(subset[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])

        return result
