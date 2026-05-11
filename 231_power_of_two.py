#Leetcode :  231 Power Of Two
#Approach :
#If n <= 0, return False.
#If n == 1, return True.
#If n is odd, return False.
#Otherwise, recursively divide n by 2 and check again.
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        if n == 1 :
            return True
        if n%2 != 0:
            return False

        return self.isPowerOfTwo(n//2)
      
