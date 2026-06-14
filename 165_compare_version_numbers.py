# LeetCode 165: Compare Version Numbers | Two Pointers / Split Revisions

# Approach:
# Each version consists of revisions separated by '.'.
#
# 1. Split both version strings using '.'.
#
# 2. Traverse both revision lists simultaneously.
#    - Convert each revision to an integer.
#    - Leading zeros are automatically ignored by int().
#
# 3. If one version has fewer revisions:
#    - Treat missing revisions as 0.
#
# 4. Compare corresponding revisions:
#    - If revision1 > revision2, return 1.
#    - If revision1 < revision2, return -1.
#
# 5. If all revisions are equal, return 0.
#
# 6. Complexity:
#    - Time Complexity: O(n + m)
#    - Space Complexity: O(n + m)


class Solution(object):
    def compareVersion(self, version1, version2):

        v1 = version1.split('.')
        v2 = version2.split('.')

        n = max(len(v1), len(v2))

        for i in range(n):

            rev1 = int(v1[i]) if i < len(v1) else 0
            rev2 = int(v2[i]) if i < len(v2) else 0

            if rev1 > rev2:
                return 1

            if rev1 < rev2:
                return -1

        return 0
