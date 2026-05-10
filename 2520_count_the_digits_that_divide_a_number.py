#Leetcode : 2520 Count the digits that divide a number
#Approach :
#We use a temporary variable temp to traverse each digit of the number without modifying the original number.
#Using modulo (% 10), we extract the last digit one by one.
#For every extracted digit, we check whether it divides the original number
#If it divides perfectly, we increment the count.
#Then we remove the last digit using integer division (// 10) and continue until all digits are processed.
#Finally, we return the total count of digits that evenly divide the number.

class Solution(object):
    def countDigits(self, num):
        temp = num
        ans = 0
        while temp>0:
            r = temp%10
            if num % r == 0:
                ans+=1
            temp//= 10
        return ans
