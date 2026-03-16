# LeetCode 15: 3Sum (Two Pointer Approach)
#Approach:
#• Sort the array.
#• Fix one element nums[i].
#• Use two pointers (left = i+1, right = n-1) to find pairs with sum = -nums[i].
#• If sum == 0 → store triplet.
#• If sum < 0 → move left pointer.
#• If sum > 0 → move right pointer.
#• Skip duplicate elements to avoid repeated triplets.

#Time Complexity: O(n²)  
#Space Complexity: O(1) (excluding output)

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):

            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                   
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                   
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
