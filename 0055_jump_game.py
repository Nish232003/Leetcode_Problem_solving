#LeetCode 55: Jump Game

#Approach:
#The array represents the maximum jump length from each position.
#We use a greedy approach to track the farthest index reachable.
#Traverse the array and update max_reach at each step.
#If at any index i, i > max_reach, we cannot move forward, so return False.
#Otherwise, update max_reach = max(max_reach, i + nums[i]).
#If we complete traversal, it means we can reach the last index.

#Time Complexity: O(n)
#Space Complexity: O(1)

class Solution(object):
    def canJump(self, nums):
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

        return True
