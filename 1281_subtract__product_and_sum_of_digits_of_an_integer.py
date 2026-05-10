#Leetcode : 1281
#Approach : 

#- Create two variables:
 # - one to store the sum of digits
  #- another to store the product of digits
#- Use a temporary variable to traverse the number digit by digit.
#- Extract the last digit using modulo (% 10).
#- Add the digit to the sum variable.
#- Multiply the digit with the product variable.
#- Remove the last digit using integer division (// 10).
#- Continue until all digits are processed.
#- Finally, return the difference between product and sum.

#Time Complexity: O(d)
#Space Complexity: O(1)

class Solution(object):
    def subtractProductAndSum(self, n):
        temp = n
        sum = 0
        product = 1

        while temp>0 :
            r = temp%10
            temp//=10
            sum += r
            product *= r
        return product-sum
