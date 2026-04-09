# LeetCode: 12. Integer to Roman

# Approach:
# - Use Greedy strategy.
# - Instead of building digit by digit, always subtract the largest possible value.
# - Maintain a list of values and their corresponding Roman symbols.


class Solution(object):
    def intToRoman(self, num):
        
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        
        symbols = [
            "M","CM","D","CD",
            "C","XC","L","XL",
            "X","IX","V","IV","I"
        ]
        
        result = ""
        
        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]
        
        return result
