# LeetCode 11: Container With Most Water

# Approach:
# We use the two-pointer technique to find the maximum water container.
# Start with two pointers at the beginning (left) and end (right) of the array.
# Calculate the area formed between them using:
# width = right - left
# height = min(height[left], height[right])
# area = width * height

# To maximize area:
# - Move the pointer pointing to the smaller height inward
# - Because the smaller height limits the container

# Continue until both pointers meet.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
