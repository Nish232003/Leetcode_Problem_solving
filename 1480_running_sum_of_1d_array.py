#Leetcode : 1480  Running Sum of 1D Array 

## Approach

#* Create a new list `ans` to store the running sum values.
#* Add the first element of `nums` directly into `ans`.
#* Traverse the array from index `1` to `n-1`.
#* For each element:

 # * Add the current number to the previous running sum stored in `ans`.
  #* Append the new sum into `ans`.
#* Return the final `ans` list.


class Solution(object):
    def runningSum(self, nums):
        n = len(nums)

        ans = []
        ans.append(nums[0])

        for i in range(1, n):
            x = ans[i - 1] + nums[i]
            ans.append(x)

        return ans
