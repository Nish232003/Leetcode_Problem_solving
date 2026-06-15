# LeetCode 42: Trapping Rain Water | Two Pointers

# Approach:
# Instead of computing leftMax and rightMax arrays separately,
# we use two pointers to calculate trapped water in a single pass.
#
# 1. Initialize:
#    - left pointer at start.
#    - right pointer at end.
#    - left_max stores highest bar seen from left.
#    - right_max stores highest bar seen from right.
#
# 2. Traverse while left < right:
#
#    - If height[left] < height[right]:
#
#         • Water trapped depends on left_max.
#
#         • If current bar is smaller than left_max:
#               trapped += left_max - height[left]
#
#         • Otherwise update left_max.
#
#         • Move left pointer forward.
#
#    - Else:
#
#         • Water trapped depends on right_max.
#
#         • If current bar is smaller than right_max:
#               trapped += right_max - height[right]
#
#         • Otherwise update right_max.
#
#         • Move right pointer backward.
#
# 3. Why it works:
#    - Water at a position is determined by the smaller boundary.
#    - By processing the smaller side first, we already know the
#      limiting wall for that side.
#
# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


class Solution(object):
    def trap(self, height):

        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0

        while left < right:

            if height[left] < height[right]:

                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water
