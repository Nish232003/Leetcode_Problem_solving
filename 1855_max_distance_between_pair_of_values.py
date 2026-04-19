# LeetCode 1855: Maximum Distance Between a Pair of Values

# Approach:
# Since both arrays are non-increasing, we use two pointers.
# Start with i = 0 and j = 0.
# If nums1[i] <= nums2[j], it's a valid pair → update max distance and move j forward.
# Otherwise, move i forward to satisfy the condition.
# This ensures we explore maximum possible distance efficiently.

# Time Complexity: O(n + m)
# Space Complexity: O(1)

class Solution(object):
    def maxDistance(self, nums1, nums2):
        i = 0
        j = 0
        maxDist = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                maxDist = max(maxDist, j - i)
                j += 1
            else:
                i += 1
        
        return maxDist
