# LeetCode 164: Maximum Gap | Bucket Sort (Pigeonhole Principle)

# Approach:
# Instead of sorting the array (O(n log n)), we use Bucket Sort to achieve O(n).
#
# 1. Handle edge cases:
#    - If array has fewer than 2 elements, return 0.
#    - If all elements are identical, return 0.
#
# 2. Find:
#    - Minimum element (mn)
#    - Maximum element (mx)
#
# 3. Determine bucket size:
#    - The minimum possible maximum gap is:
#        ceil((mx - mn) / (n - 1))
#    - Use this value as bucket size.
#
# 4. Create buckets:
#    - Each bucket stores:
#        • Minimum value in that bucket
#        • Maximum value in that bucket
#
# 5. Place each number into its bucket.
#
# 6. Traverse buckets:
#    - Ignore empty buckets.
#    - Maximum gap can only occur between two non-empty buckets.
#    - Compare current bucket's minimum with previous bucket's maximum.
#
# 7. Return the largest gap found.
#
# 8. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


class Solution(object):
    def maximumGap(self, nums):

        n = len(nums)

        if n < 2:
            return 0

        mn = min(nums)
        mx = max(nums)

        if mn == mx:
            return 0

        bucket_size = max(1, (mx - mn + n - 2) // (n - 1))
        bucket_count = (mx - mn) // bucket_size + 1

        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

        for num in nums:
            idx = (num - mn) // bucket_size

            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)

        max_gap = 0
        prev_max = mn

        for bmin, bmax in buckets:

            if bmin == float('inf'):
                continue

            max_gap = max(max_gap, bmin - prev_max)
            prev_max = bmax

        return max_gap
