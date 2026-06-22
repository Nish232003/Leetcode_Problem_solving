# LeetCode 1732: Find the Highest Altitude | Prefix Sum

# Approach:
# Instead of storing all altitudes, we maintain the current altitude
# while traversing the gain array and keep track of the maximum altitude reached.

# 1. Initialize:
#    - Start at altitude 0.
#    - Set answer to 0 since the starting point is also considered.

# 2. Traverse the gain array:
#    - Add each gain value to the current altitude.
#    - Update the maximum altitude whenever a higher altitude is reached.

# 3. Return the answer:
#    - The maximum altitude encountered during the trip.

# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def largestAltitude(self, gain):

        altitude = 0
        ans = 0

        for g in gain:
            altitude += g
            ans = max(ans, altitude)

        return ans
