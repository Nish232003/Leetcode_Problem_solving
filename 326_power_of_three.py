#Leetcode : 326
#Approach : Recursion
#If n <= 0, return False.
#If n == 1, return True.
#If n % 3 != 0 return False.
#Otherwise, recursively divide n by 3 and check again.

class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n//3)
