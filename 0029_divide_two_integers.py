#LeetCode 29: Divide Two Integers | Bit Manipulation + Exponential Search

#Approach:
#Instead of repeatedly subtracting the divisor (O(n)), we optimize using bit manipulation.
#1. Handle overflow case:
#   If dividend = -2^31 and divisor = -1, the result exceeds 32-bit range,
#   so return 2^31 - 1.

#2. Determine the sign of the result using XOR:
#   Result is negative if exactly one of dividend or divisor is negative.

#3. Convert both numbers to absolute values to simplify computation.

#4. Use exponential subtraction with bit shifting:
#   - Repeatedly double the divisor using left shift.
#   - Find the largest multiple of divisor that can be subtracted from dividend.
#   - Subtract that value and add the corresponding multiple to the quotient.

#5. Repeat until dividend becomes smaller than divisor.

#6. Apply the calculated sign to the final quotient.
class Solution(object):
    def divide(self, dividend, divisor):
        
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            quotient += multiple
        
        return sign * quotient
