# LeetCode 220: Contains Duplicate III | Bucket Sort + Sliding Window

# Approach:
# Instead of comparing every pair, divide numbers into buckets of size
# (valueDiff + 1). Any two numbers satisfying |nums[i] - nums[j]| <= valueDiff
# must either lie in the same bucket or in neighboring buckets.

# 1. Handle edge case:
#    - If valueDiff < 0, return False.

# 2. Initialize:
#    - Create a dictionary 'buckets' to store bucket_id -> number.
#    - Bucket size = valueDiff + 1.

# 3. Traverse the array:
#    - Find the bucket corresponding to the current number.
#    - If the bucket already contains a number, return True.
#    - Check adjacent buckets (bucket-1 and bucket+1):
#        • If the difference between numbers is <= valueDiff,
#          return True.
#    - Insert the current number into its bucket.

# 4. Maintain sliding window:
#    - Remove the element whose index becomes greater than indexDiff
#      distance away.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(indexDiff)


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):

        if valueDiff < 0:
            return False

        bucket_size = valueDiff + 1
        buckets = {}

        for i, num in enumerate(nums):

            bucket_id = num // bucket_size
            if num < 0:
                bucket_id -= 1

            if bucket_id in buckets:
                return True

            if (bucket_id - 1 in buckets and
                abs(num - buckets[bucket_id - 1]) <= valueDiff):
                return True

            if (bucket_id + 1 in buckets and
                abs(num - buckets[bucket_id + 1]) <= valueDiff):
                return True

            buckets[bucket_id] = num

            if i >= indexDiff:
                old_num = nums[i - indexDiff]
                old_bucket = old_num // bucket_size
                if old_num < 0:
                    old_bucket -= 1
                del buckets[old_bucket]

        return False
