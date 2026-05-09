###Leetcode : 412 fizz buzz
###Approach :
#We iterate from 1 to n and check each number using if-elif conditions.
#If a number is divisible by both 3 and 5, add "FizzBuzz"
#Else if divisible by 3, add "Fizz"
#Else if divisible by 5, add "Buzz"
#Otherwise add the number as a string
class Solution(object):
    def fizzBuzz(self, n):
        ans = []
        for i in range(1, n+1):
            if i%3 == 0 and  i%5==0: 
              ans.append("FizzBuzz")
            elif i%3 == 0 :
                ans.append("Fizz")
            elif i%5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
