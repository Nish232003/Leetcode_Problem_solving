# LeetCode 84: Largest Rectangle in Histogram | Monotonic Increasing Stack

# Approach:
# The key idea is to find, for each bar, how far it can extend left and right
# while still being the minimum height in that range.

# We use a monotonic increasing stack to store indices of bars.

# 1. Stack maintains increasing heights:
#    - Indices of bars in increasing order of height.

# 2. When current height is smaller:
#    - It means we found the right boundary for stack top.
#    - Pop and calculate area:
#         height = popped bar height
#         width = current index - previous stack top - 1

# 3. After traversal:
#    - Process remaining stack elements as they extend to end.

# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)

class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area, h * width)

            stack.append(i)

        while stack:
            h = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = n - left - 1
            max_area = max(max_area, h * width)

        return max_area
