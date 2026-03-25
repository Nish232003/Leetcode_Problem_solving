#LeetCode 16: 3Sum Closest
#1. Idea:
  # - Instead of brute force (O(n^3)), we optimize using sorting + two pointers.
   #- Fix one element and solve remaining as 2Sum Closest.

#2. Steps:
 #  - Sort the array.
  # - Initialize closest_sum using first 3 elements.
   #- Loop through each element (i):
    #   - Use two pointers:
     #      left = i + 1
      #     right = n - 1
       #- Calculate current_sum.
      ## - Update closest_sum if better.
       #3- Move pointers:
           #if current_sum < target → left++
           #if current_sum > target → right--
          # if equal → return immediately
#3. Edge Case:
#- If array length < 3 → not possible (handled by constraints).

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

      
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  

        return closest_sum
