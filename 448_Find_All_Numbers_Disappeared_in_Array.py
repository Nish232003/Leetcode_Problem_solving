#LeetCode 448 - Find All Numbers Disappeared in an Array
#Approach: In-place Array Marking (Index Mapping)

#Time Complexity: O(n)
#Space Complexity: O(1) (excluding output list)


class Solution:
    def findDisappearedNumbers(self, nums):

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result


