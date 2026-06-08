# LeetCode 77: Combinations | Backtracking

# Approach:
# We need to generate all possible combinations of k numbers
# chosen from the range [1, n].
#
# We use Backtracking:
#
# 1. Maintain a current combination 'path'.
#
# 2. Start choosing numbers from 'start' to n:
#    - Add the current number to path.
#    - Recursively build the remaining combination.
#    - Remove the last number (backtrack) to explore other choices.
#
# 3. Base Case:
#    - If the length of path becomes k,
#      we have found a valid combination.
#    - Add a copy of path to the answer.
#
# 4. Continue exploring all possibilities.
#
# 5. Complexity:
#    - Time Complexity: O(C(n, k) * k)
#      (There are C(n, k) combinations and copying each takes O(k))
#    - Space Complexity: O(k)
#      (Recursion stack + current combination)


class Solution(object):
    def combine(self, n, k):

        result = []

        def backtrack(start, path):

            if len(path) == k:
                result.append(path[:])
                return

            for num in range(start, n + 1):

                path.append(num)

                backtrack(num + 1, path)

                path.pop()

        backtrack(1, [])

        return result
