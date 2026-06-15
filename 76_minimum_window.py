# LeetCode 76: Minimum Window Substring | Sliding Window

# Approach:
# We use the Sliding Window technique to find the smallest substring
# that contains all characters of t (including duplicates).
#
# 1. Store frequency of characters in t using a hashmap.
#
# 2. Expand the window:
#    - Move the right pointer.
#    - Count characters entering the window.
#
# 3. Track validity:
#    - formed = number of characters whose required frequency
#      has been satisfied.
#    - required = total unique characters in t.
#
# 4. Shrink the window:
#    - When formed == required,
#      current window contains all characters.
#    - Update minimum answer.
#    - Move left pointer to minimize the window.
#
# 5. Continue until right reaches the end.
#
# 6. Complexity:
#    - Time Complexity: O(m + n)
#    - Space Complexity: O(k)
#      where k = number of unique characters.


from collections import Counter


class Solution(object):
    def minWindow(self, s, t):

        if not s or not t:
            return ""

        target = Counter(t)

        required = len(target)
        formed = 0

        window = {}

        left = 0

        min_len = float('inf')
        start = 0

        for right in range(len(s)):

            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in target and window[char] == target[char]:
                formed += 1

            while left <= right and formed == required:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]

                window[left_char] -= 1

                if (left_char in target and
                        window[left_char] < target[left_char]):
                    formed -= 1

                left += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]
