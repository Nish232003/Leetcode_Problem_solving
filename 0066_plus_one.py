#LeetCode 66: Plus One

#Approach:
#The digits array represents a large integer where each element is a digit.
#To add 1 to the number, we simulate the manual addition process starting
#from the least significant digit (rightmost).

#Time Complexity: O(n)
#Space Complexity: O(1)

class Solution(object):
    def plusOne(self, digits):
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits
