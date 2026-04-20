#Leetcode : 2079 TWO FURTHEST HOUSE WITH DIFFERENT COLORS
#Approach:
#Fix i = 0, try all j from right → find first different color
#Fix j = n-1, try all i from left → find first different color
#Take maximum of both distances

class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)
        ans = 0

        for j in range(n-1 , -1 , -1):
            if colors[j] != colors[0]:
                ans = max(ans , j-0)
                break
        
        for i in range(n):
            if colors[i] != colors[n-1]:
                ans = max(ans , (n-1) - i)
                break
        return ans
        
