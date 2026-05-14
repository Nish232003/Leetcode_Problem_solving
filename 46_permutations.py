# LeetCode 46: Permutations 

# Approach:
# Instead of generating permutations using built-in libraries, we use
# backtracking to recursively build every possible arrangement.

# 1. Initialize:
#    - Create an empty list 'answer' to store all permutations.

# 2. Backtracking Function:
#    - 'current' stores the current permutation being formed.
#    - 'remaining' stores elements still available for selection.

# 3. Base Case:
#    - If no elements are left in 'remaining',
#      a complete permutation is formed.
#    - Append a copy of 'current' into 'answer'.

# 4. Recursive Exploration:
#    - Traverse every element in 'remaining'.
#    - Pick one element and add it to 'current'.
#    - Recursively generate permutations for the leftover elements.
#    - Remove the last element (backtrack) to try other possibilities.

# 5. Complexity:
#    - Time Complexity: O(n!)
#    - Space Complexity: O(n)


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        answer = []

        def backtrack(current, remaining):

            if len(remaining) == 0:
                answer.append(current[:])
                return

            for i in range(len(remaining)):

                current.append(remaining[i])

                next_remaining = remaining[:i] + remaining[i + 1:]

                backtrack(current, next_remaining)

                current.pop()

        backtrack([], nums)

        return answer
