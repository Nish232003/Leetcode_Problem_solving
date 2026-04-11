# LeetCode 57: Insert Interval | Linear Scan + Merge

# Approach:
# Instead of sorting (already sorted), we do a single linear pass
# in three phases: skip non-overlapping left, merge overlapping, append remaining.

# 1. Handle non-overlapping intervals on the LEFT:
#    - If intervals[i][1] < newInterval[0], no overlap → add as-is.

# 2. Merge overlapping intervals:
#    - While intervals[i][0] <= newInterval[1], expand newInterval
#      using min/max on both ends.

# 3. Append remaining:
#    - All intervals to the right of merged region → add as-is.

# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


class Solution(object):
    def insert(self, intervals, newInterval):

        result = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i += 1

        return result
