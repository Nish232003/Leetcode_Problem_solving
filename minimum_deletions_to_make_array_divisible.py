# Leetcode : Minimum Deletions to Make Array Divisible
# Leetcode link : https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

# Approach :
# The goal is to delete minimum elements from nums such that the smallest remaining
# element divides all elements of numsDivide.
# First compute the GCD of numsDivide, because any valid number must divide this GCD.
# Then sort nums and find the first element that divides the GCD.
# The index of that element represents the minimum deletions required.

# Time complexity : O(n log n)
# Space complexity : O(1)

# Steps :
# 1. Compute GCD of all elements in numsDivide.
# 2. Sort the nums array.
# 3. Traverse nums from smallest element.
# 4. For each element check if it divides the GCD.
# 5. If yes -> return its index (minimum deletions).
# 6. If no element divides the GCD -> return -1.

from functools import reduce

class Solution(object):
    def minOperations(self, nums, numsDivide):
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        g = reduce(gcd, numsDivide)
        nums.sort()

        for i, num in enumerate(nums):
            if g % num == 0:
                return i
        
        return -1
