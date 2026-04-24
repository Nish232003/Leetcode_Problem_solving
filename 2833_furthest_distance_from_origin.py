#Leetcode 2833 : Furthest Distance from Origin using greedy + counting approach

#- Count occurrences of 'L', 'R', and '_' in the input string
#- Observe that 'L' and 'R' moves cancel each other partially
#- Net displacement from fixed moves is abs(L - R)
#- Use all '_' moves in the direction that maximizes distance
#- Final distance = abs(L - R) + number of '_'

class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        L = moves.count('L')
        R = moves.count('R')
        U = moves.count('_')
        
        return abs(L - R) + U
