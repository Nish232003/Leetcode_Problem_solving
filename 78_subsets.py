# LeetCode 78: Subsets | Backtracking

# Approach:
# We need to generate all possible subsets (power set) of the given array.
#
# For each element, we have two choices:
# 1. Include it in the current subset.
# 2. Exclude it from the current subset.
#
# We use Backtracking:
#
# 1. Start with an empty subset.
#
# 2. At every recursive call:
#    - Add the current subset to the result.
#    - Try including each remaining element one by one.
#
# 3. For each choice:
#    - Add the element to the current subset.
#    - Recurse for the next elements.
#    - Remove the element (backtrack) to explore other possibilities.
#
# 4. Since all elements are unique, no duplicate subsets are generated.
#
# 5. Complexity:
#    - Time Complexity: O(n * 2^n)
#      (There are 2^n subsets and copying each subset takes O(n))
#    - Space Complexity: O(n)
#      (Recursion stack + current subset)


class Solution(object):
    def subsets(self, nums):

        result = []

        def backtrack(start, path):

            result.append(path[:])

            for i in range(start, len(nums)):

                path.append(nums[i])

                backtrack(i + 1, path)

                path.pop()

        backtrack(0, [])

        return result
