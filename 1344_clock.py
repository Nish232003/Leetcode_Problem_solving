# LeetCode 1344: Angle Between Hands of a Clock | Math

# Approach:
# Instead of simulating the clock, we calculate the positions of the
# hour and minute hands directly and find the smaller angle between them.

# 1. Compute minute hand angle:
#    - The minute hand moves 360° in 60 minutes.
#    - minute_angle = 6 × minutes

# 2. Compute hour hand angle:
#    - The hour hand moves 360° in 12 hours.
#    - It moves 30° per hour and 0.5° per minute.
#    - hour_angle = 30 × (hour % 12) + 0.5 × minutes

# 3. Find the absolute difference:
#    - angle = |hour_angle - minute_angle|

# 4. Return the smaller angle:
#    - Since a circle is 360°, the required answer is
#      min(angle, 360 - angle)

# 5. Complexity:
#    - Time Complexity: O(1)
#    - Space Complexity: O(1)


class Solution(object):
    def angleClock(self, hour, minutes):

        minute_angle = 6 * minutes
        hour_angle = 30 * (hour % 12) + 0.5 * minutes

        angle = abs(hour_angle - minute_angle)

        return min(angle, 360 - angle)
