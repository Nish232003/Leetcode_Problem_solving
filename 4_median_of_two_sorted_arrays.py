#LeetCode #4: Median of Two Sorted Arrays

#Approach:
#Used binary search on the smaller array to find a correct partition between the two sorted arrays
#Time Complexity: O(log(min(m,n)))
#Space Complexity: O(1)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        # Ensure binary search is applied on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)

        low = 0
        high = x

        while low <= high:

            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:

                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) +
                            min(minRightX, minRightY)) / 2.0
                else:
                    return max(maxLeftX, maxLeftY)

            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1
