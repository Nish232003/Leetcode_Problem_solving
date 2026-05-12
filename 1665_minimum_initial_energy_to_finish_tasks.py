# LeetCode 1665: Minimum Initial Energy to Finish Tasks | Greedy Sorting

# Approach:
# Instead of trying every possible task order, we use a greedy strategy
# to minimize the initial energy required.
#
# We prioritize tasks that require a larger extra energy buffer:
#     (minimum - actual)
#
# This ensures difficult tasks are completed earlier when more energy
# is available.

# 1. Sort tasks:
#    - Sort all tasks in descending order of:
#          (minimum - actual)
#
# 2. Initialize:
#    - 'energy' stores the minimum initial energy required.
#    - 'current' stores currently available energy.

# 3. Process each task:
#    - If current energy is less than the task's minimum requirement:
#         increase initial energy accordingly.
#    - Perform the task:
#         subtract actual energy consumed.

# 4. Return result:
#    - Final 'energy' represents the minimum initial energy needed.

# 5. Complexity:
#    - Time Complexity: O(n log n)
#    - Space Complexity: O(1) excluding sorting


class Solution(object):
    def minimumEffort(self, tasks):

        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        energy = 0
        current = 0

        for actual, minimum in tasks:

            if current < minimum:
                energy += (minimum - current)
                current = minimum

            current -= actual

        return energy
