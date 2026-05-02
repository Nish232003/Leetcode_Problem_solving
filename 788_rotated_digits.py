# LeetCode 788: Rotated Digits

# Approach:
# 1. Valid digits after rotation:
#    - Same after rotation: 0, 1, 8
#    - Change after rotation: 2, 5, 6, 9
#    - Invalid digits: 3, 4, 7
#
# 2. A number is "good" if:
#    - All digits are valid
#    - At least one digit changes after rotation
#
# 3. For each number from 1 to n:
#    - Check digits
#    - If invalid digit → skip
#    - If at least one changing digit → count++

class Solution(object):
    def rotatedDigits(self, n):
        
        same = {'0', '1', '8'}
        
        
        change = {'2', '5', '6', '9'}
        
        count = 0
        
        for num in range(1, n + 1):
            s = str(num)
            is_valid = True
            has_change = False
            
            for ch in s:
                if ch in change:
                    has_change = True
                elif ch not in same:
                    is_valid = False
                    break
            
            if is_valid and has_change:
                count += 1
        
        return count
