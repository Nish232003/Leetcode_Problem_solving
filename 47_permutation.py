# LeetCode 47: Permutations II | Backtracking + Duplicate Handling

# Approach:
# We generate all unique permutations using backtracking.
# Since duplicates may exist, we first sort the array so that
# duplicate elements appear together.

# 1. Sort the array:
#    - Helps detect duplicates easily.

# 2. Use backtracking:
#    - Maintain:
#         • 'path' for current permutation
#         • 'used' array to track visited elements

# 3. Skip duplicates:
#    - If current element is same as previous element
#      and previous duplicate was NOT used in this recursion level,
#      skip it to avoid repeated permutations.

# 4. Base case:
#    - If path length becomes equal to nums length,
#      store the permutation.

# 5. Complexity:
#    - Time Complexity: O(n * n!)
#    - Space Complexity: O(n)


class Solution(object):
    def permuteUnique(self, nums):

        nums.sort()

        result = []
        used = [False] * len(nums)

        
        def backtrack(path):

            
            if len(path) == len(nums):
                result.append(path[:])
                return

            
            for i in range(len(nums)):

                
                if used[i]:
                    continue

                
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                
                used[i] = True
                path.append(nums[i])

                
                backtrack(path)

                
                path.pop()
                used[i] = False

        
        backtrack([])

        return result
