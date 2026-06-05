# LeetCode 134: Gas Station | Greedy

# Approach:
# Instead of checking every station as a starting point, we use a greedy approach.

# 1. Check feasibility:
#    - If total gas available is less than total cost required,
#      completing the circuit is impossible, so return -1.

# 2. Initialize:
#    - start = 0 → current candidate starting station.
#    - tank = 0 → current gas left while traversing.

# 3. Traverse all stations:
#    - Add gas[i] - cost[i] to tank.
#    - If tank becomes negative:
#        • Current start cannot complete the journey.
#        • Any station between start and i also cannot be a valid start.
#        • Set start = i + 1.
#        • Reset tank = 0.

# 4. Return:
#    - After one traversal, 'start' will be the unique valid answer.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def canCompleteCircuit(self, gas, cost):

        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0

        return start
