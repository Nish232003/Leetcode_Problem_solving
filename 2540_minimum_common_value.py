# LeetCode 2540: Minimum Common Value | Two Pointer Approach

# Approach:
# Since both arrays are already sorted in non-decreasing order,
# we can efficiently find the smallest common element using two pointers.

# 1. Initialize two pointers:
#    - i for nums1
#    - j for nums2

# 2. Traverse both arrays:
#    - If nums1[i] == nums2[j]:
#         • We found the smallest common value.
#         • Return that value immediately.
#
#    - If nums1[i] < nums2[j]:
#         • Move pointer i forward because a smaller value
#           cannot match a larger one later.
#
#    - Else:
#         • Move pointer j forward.

# 3. If traversal ends without any match:
#    - Return -1.

# 4. Complexity:
#    - Time Complexity: O(n + m)
#    - Space Complexity: O(1)


class Solution(object):
    def getCommon(self, nums1, nums2):

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] == nums2[j]:
                return nums1[i]

            elif nums1[i] < nums2[j]:
                i += 1

            else:
                j += 1

        return -1
